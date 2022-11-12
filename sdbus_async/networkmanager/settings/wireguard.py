# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses-jinja.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple
from .base import NetworkManagerSettingsMixin
from .datatypes import WireguardPeers


@dataclass
class WireguardSettings(NetworkManagerSettingsMixin):
    """WireGuard Settings"""

    fwmark: Optional[int] = field(
        metadata={
            'dbus_name': 'fwmark',
            'dbus_type': 'u',
        },
        default=None,
    )
    """The use of fwmark is optional and is by default off. Setting it to 0
    disables it. Otherwise, it is a 32-bit fwmark for outgoing packets.

    Note that "ip4-auto-default-route" or "ip6-auto-default-route"
    enabled, implies to automatically choose a fwmark."""
    ip4_auto_default_route: Optional[int] = field(
        metadata={
            'dbus_name': 'ip4-auto-default-route',
            'dbus_type': 'i',
        },
        default=None,
    )
    """Whether to enable special handling of the IPv4 default route. If
    enabled, the IPv4 default route from wireguard.peer-routes will be
    placed to a dedicated routing-table and two policy routing rules
    will be added. The fwmark number is also used as routing-table for
    the default-route, and if fwmark is zero, an unused fwmark/table is
    chosen automatically. This corresponds to what wg-quick does with
    Table=auto and what WireGuard calls "Improved Rule-based Routing".

    Note that for this automatism to work, you usually don't want to set
    ipv4.gateway, because that will result in a conflicting default
    route.

    Leaving this at the default will enable this option automatically if
    ipv4.never-default is not set and there are any peers that use a
    default-route as allowed-ips. Since this automatism only makes sense
    if you also have a peer with an /0 allowed-ips, it is usually not
    necessary to enable this explicitly. However, you can disable it if
    you want to configure your own routing and rules."""
    ip6_auto_default_route: Optional[int] = field(
        metadata={
            'dbus_name': 'ip6-auto-default-route',
            'dbus_type': 'i',
        },
        default=None,
    )
    """Like ip4-auto-default-route, but for the IPv6 default route."""
    listen_port: Optional[int] = field(
        metadata={
            'dbus_name': 'listen-port',
            'dbus_type': 'u',
        },
        default=None,
    )
    """The listen-port. If listen-port is not specified, the port will be
    chosen randomly when the interface comes up."""
    mtu: Optional[int] = field(
        metadata={
            'dbus_name': 'mtu',
            'dbus_type': 'u',
        },
        default=None,
    )
    """If non-zero, only transmit packets of the specified size or smaller,
    breaking larger packets up into multiple fragments.

    If zero a default MTU is used. Note that contrary to wg-quick's MTU
    setting, this does not take into account the current routes at the
    time of activation."""
    peer_routes: Optional[bool] = field(
        metadata={
            'dbus_name': 'peer-routes',
            'dbus_type': 'b',
        },
        default=None,
    )
    """Whether to automatically add routes for the AllowedIPs ranges of the
    peers. If TRUE (the default), NetworkManager will automatically add
    routes in the routing tables according to ipv4.route-table and
    ipv6.route-table. Usually you want this automatism enabled. If
    FALSE, no such routes are added automatically. In this case, the
    user may want to configure static routes in ipv4.routes and
    ipv6.routes, respectively.

    Note that if the peer's AllowedIPs is "0.0.0.0/0" or "::/0" and the
    profile's ipv4.never-default or ipv6.never-default setting is
    enabled, the peer route for this peer won't be added automatically."""
    peers: Optional[List[WireguardPeers]] = field(
        metadata={
            'dbus_name': 'peers',
            'dbus_type': 'aa{sv}',
            'dbus_inner_class': WireguardPeers,
        },
        default=None,
    )
    """Array of dictionaries for the WireGuard peers."""
    private_key: Optional[str] = field(
        metadata={
            'dbus_name': 'private-key',
            'dbus_type': 's',
        },
        default=None,
    )
    """The 256 bit private-key in base64 encoding."""
    private_key_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'private-key-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "private-key" property."""
