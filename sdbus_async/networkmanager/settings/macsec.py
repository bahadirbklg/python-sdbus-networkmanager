# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class MacsecSettings(NetworkManagerSettingsMixin):
    """MACSec Settings"""

    encrypt: Optional[bool] = field(
        metadata={'dbus_name': 'encrypt', 'dbus_type': 'b'},
        default=True,
    )
    mka_cak: Optional[str] = field(
        metadata={'dbus_name': 'mka-cak', 'dbus_type': 's'},
        default=None,
    )
    mka_cak_flags: Optional[int] = field(
        metadata={'dbus_name': 'mka-cak-flags', 'dbus_type': 'i'},
        default=None,
    )
    mka_ckn: Optional[str] = field(
        metadata={'dbus_name': 'mka-ckn', 'dbus_type': 's'},
        default=None,
    )
    mode: Optional[int] = field(
        metadata={'dbus_name': 'mode', 'dbus_type': 'i'},
        default=None,
    )
    parent: Optional[str] = field(
        metadata={'dbus_name': 'parent', 'dbus_type': 's'},
        default=None,
    )
    port: Optional[int] = field(
        metadata={'dbus_name': 'port', 'dbus_type': 'i'},
        default=1,
    )
    send_sci: Optional[bool] = field(
        metadata={'dbus_name': 'send-sci', 'dbus_type': 'b'},
        default=True,
    )
    validation: Optional[int] = field(
        metadata={'dbus_name': 'validation', 'dbus_type': 'i'},
        default=2,
    )