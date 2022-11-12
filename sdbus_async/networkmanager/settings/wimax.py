# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses-jinja.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class WimaxSettings(NetworkManagerSettingsMixin):
    """WiMax Settings"""

    mac_address: Optional[bytes] = field(
        metadata={
            'dbus_name': 'mac-address',
            'dbus_type': 'ay',
        },
        default=None,
    )
    """If specified, this connection will only apply to the WiMAX device whose
    MAC address matches. This property does not change the MAC address
    of the device (known as MAC spoofing)."""
    network_name: Optional[str] = field(
        metadata={
            'dbus_name': 'network-name',
            'dbus_type': 's',
        },
        default=None,
    )
    """Network Service Provider (NSP) name of the WiMAX network this connection
    should use."""
