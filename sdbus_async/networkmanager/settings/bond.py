# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class BondSettings(NetworkManagerSettingsMixin):
    """Bonding Settings"""

    interface_name: Optional[str] = field(
        metadata={'dbus_name': 'interface-name', 'dbus_type': 's'},
        default=None,
    )
    options: Optional[Dict[str, str]] = field(
        metadata={'dbus_name': 'options', 'dbus_type': 'a{ss}'},
        default={'Mode': 'Balance-Rr'},
    )
