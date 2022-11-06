#!/usr/bin/env python
# SPDX-License-Identifier: LGPL-2.1-or-later

# Gerating nm-settings-docs-dbus.xml from NetworkManager source code
# 1. meson setup \
#       -Dselinux=false \
#       -Dqt=false \
#       -Dintrospection=true \
#       -Ddocs=true \
#       build
# 2. cd build
# 3. ninja man/nm-settings-docs-dbus.xml
from __future__ import annotations

import builtins
import keyword
from argparse import ArgumentParser
from functools import cached_property
from pathlib import Path
from re import Pattern
from re import compile as regex_compile
from textwrap import fill
from typing import List, Optional
from xml.etree.ElementTree import Element, parse

from jinja2 import Environment

dbus_to_python_extra_typing_imports = {
    "as": ("List", ),
    "au": ("List", ),
    "a{ss}": ("Dict", ),
    "aa{sv}": ("List", "Tuple", "Any"),
    "aau": ("List", ),
    "aay": ("List", )
}

dbus_to_python_type_map = {
    "b": "bool",
    "s": "str",
    "i": "int",
    "u": "int",
    "t": "int",
    "x": "int",
    "y": "int",
    "as": "List[str]",
    "au": "List[int]",
    "ay": "bytes",
    "a{ss}": "Dict[str, str]",
    "aa{sv}": "List[Tuple[str, Any]]",
    "aau": "List[List[int]]",
    "aay": "List[bytes]",
    # Legacy types:
    "a(ayuay)": "array of legacy IPv6 address struct",
    "a(ayuayu)": "array of legacy IPv6 route struct",
}

dbus_name_type_map = {
    'array of array of uint32': 'aau',
    'array of byte array': 'aay',
    'array of legacy IPv6 address struct': 'a(ayuay)',
    'array of legacy IPv6 address struct (a(ayuay))': 'a(ayuay)',
    'array of legacy IPv6 route struct': 'a(ayuayu)',
    'array of legacy IPv6 route struct (a(ayuayu))': 'a(ayuayu)',
    'array of string': 'as',
    'array of strings': 'as',
    'array of uint32': 'au',
    'array of vardict': 'aa{sv}',
    "array of 'a{sv}'": 'aa{sv}',  # wireguard.peers uses this, fix NM upstream
    'boolean': 'b',
    'byte': 'y',
    'byte array': 'ay',
    'dict of string to string': 'a{ss}',
    'int32': 'i',
    'int64': 'x',
    'string': 's',
    'uint32': 'u',
    'uint64': 't',
}

python_name_replacements = {
    'type': 'connection_type',
    'id': 'pretty_id',
}


array_of_vardicts_python_classes: dict[str, str] = {
    'peers': 'WireguardPeers',
    'vlans': 'Vlans',
    'address-data': 'AddressData',
    'route-data': 'RouteData',
    'routing-rules': 'RoutingRules',
    'vfs': 'Vfs',
    'qdiscs': 'Qdiscs',
    'tfilters': 'Tfilters',
    'link-watchers': 'LinkWatchers',
}


def must_replace_name(name: str) -> bool:
    return (keyword.iskeyword(name)
            or keyword.issoftkeyword(name)
            or hasattr(builtins, name))


class NmSettingPropertyIntrospection:
    def __init__(self, name: str,
                 description: str,
                 name_upper: str,
                 dbus_type: str,
                 parent: NmSettingsIntrospection,
                 default: Optional[str] = None,
                 ) -> None:
        self.name = name
        self.description = description
        self.name_upper = name_upper
        self.python_name = name_upper.lower()
        self.dbus_type = dbus_type
        self.default = default

        if must_replace_name(self.python_name):
            self.python_name = (f"{parent.name_upper.lower()}"
                                f"_{self.python_name}")

        extra_typing = dbus_to_python_extra_typing_imports.get(dbus_type)
        if extra_typing is not None:
            parent.typing_imports.update(extra_typing)

    @cached_property
    def python_type(self) -> str:
        if self.dbus_type == 'aa{sv}':
            return f"List[{array_of_vardicts_python_classes[self.name]}]"

        return dbus_to_python_type_map[self.dbus_type]

    @cached_property
    def python_inner_class(self) -> Optional[str]:
        return array_of_vardicts_python_classes.get(self.name)


class NmSettingsIntrospection:
    def __init__(self, name: str, description: str, name_upper: str,
                 ) -> None:
        self.name = name
        self.description = description
        self.name_upper = name_upper
        self.python_class_name = name.capitalize() + 'Settings'

        self.typing_imports = {'Optional'}

        self.properties: List[NmSettingPropertyIntrospection] = []

    @cached_property
    def snake_name(self) -> str:
        return self.name_upper.lower()

    @cached_property
    def datatypes_imports(self) -> list[str]:
        datatypes_found: list[str] = []
        for x in self.properties:
            if (datatype := x.python_inner_class) is not None:
                datatypes_found.append(datatype)

        return datatypes_found


def extract_and_format_option_description(node: Element) -> str:
    paragraphs: list[str] = []
    for para in node.iter('para'):
        paragraphs.append(fill(para.text, width=72))

    return '\n\n'.join(paragraphs)


def convert_property(node: Element,
                     parent: NmSettingsIntrospection
                     ) -> Optional[NmSettingPropertyIntrospection]:
    options = node.attrib.copy()

    try:
        unconverted_type = options.pop('type')
    except KeyError:
        return None

    try:
        dbus_type = dbus_name_type_map[unconverted_type]
    except KeyError:
        dbus_type = dbus_name_type_map[unconverted_type.split('(')[1][:-1]]

    options['dbus_type'] = dbus_type
    options['description'] = extract_and_format_option_description(node)

    return NmSettingPropertyIntrospection(**options, parent=parent)


def generate_introspection(root: Element) -> List[NmSettingsIntrospection]:
    settings_introspection: List[NmSettingsIntrospection] = []
    for setting_node in root:
        setting = NmSettingsIntrospection(**setting_node.attrib)

        for x in setting_node:
            new_property = convert_property(x, setting)
            if new_property is not None:
                setting.properties.append(new_property)

        settings_introspection.append(setting)

    return settings_introspection


setttngs_template_str = """# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses-jinja.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import {{ setting.typing_imports|sort|join(', ') }}
from .base import NetworkManagerSettingsMixin
{% if setting.datatypes_imports -%}
from .datatypes import {{ setting.datatypes_imports|sort|join(', ') }}
{% endif %}

@dataclass
class {{ setting.python_class_name }}(NetworkManagerSettingsMixin):
    \"""{{ setting.description }}\"""
{% for property in setting.properties %}
    {{ property.python_name }}: Optional[{{ property.python_type }}] = field(
        metadata={
            'dbus_name': '{{ property.name }}',
            'dbus_type': '{{ property.dbus_type }}',
{%- if property.python_inner_class %}
            'dbus_inner_class': {{ property.python_inner_class }},
{%- endif %}
        },
        default=None,
    ){% endfor %}

"""

jinja_env = Environment()
settings_template = jinja_env.from_string(setttngs_template_str)


def main(
        settings_xml_path: Path,
        regex_filter: Optional[Pattern] = None,
) -> None:
    tree = parse(settings_xml_path)
    introspection = generate_introspection(tree.getroot())

    settings_dir = Path('./sdbus_async/networkmanager/settings/')
    for setting in introspection:

        if regex_filter is not None:
            if not regex_filter.match(setting.snake_name):
                continue

        setting_py_file = settings_dir / (setting.snake_name + '.py')
        with open(setting_py_file, mode='w') as f:
            f.write(settings_template.render(setting=setting))


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        'settings_xml_path',
        type=Path,
        default=Path('./nm-settings-docs-dbus.xml'),
    )
    arg_parser.add_argument(
        '--regex-filter',
        type=regex_compile,
    )

    args = arg_parser.parse_args()

    main(**vars(args))
