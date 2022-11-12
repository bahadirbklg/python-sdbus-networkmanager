# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses-jinja.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple
from .base import NetworkManagerSettingsMixin
from .datatypes import AddressData, RouteData, RoutingRules


@dataclass
class Ipv4Settings(NetworkManagerSettingsMixin):
    """IPv4 Settings"""

    address_data: Optional[List[AddressData]] = field(
        metadata={
            'dbus_name': 'address-data',
            'dbus_type': 'aa{sv}',
            'dbus_inner_class': AddressData,
        },
        default=None,
    )
    """Array of IPv4 addresses. Each address dictionary contains at least
    'address' and 'prefix' entries, containing the IP address as a
    string, and the prefix length as a uint32. Additional attributes may
    also exist on some addresses."""
    addresses: Optional[List[List[int]]] = field(
        metadata={
            'dbus_name': 'addresses',
            'dbus_type': 'aau',
        },
        default=None,
    )
    """Array of IP addresses."""
    dad_timeout: Optional[int] = field(
        metadata={
            'dbus_name': 'dad-timeout',
            'dbus_type': 'i',
        },
        default=None,
    )
    """Timeout in milliseconds used to check for the presence of duplicate IP
    addresses on the network.  If an address conflict is detected, the
    activation will fail.  A zero value means that no duplicate address
    detection is performed, -1 means the default value (either
    configuration ipvx.dad-timeout override or zero).  A value greater
    than zero is a timeout in milliseconds.

    The property is currently implemented only for IPv4."""
    dhcp_client_id: Optional[str] = field(
        metadata={
            'dbus_name': 'dhcp-client-id',
            'dbus_type': 's',
        },
        default=None,
    )
    """A string sent to the DHCP server to identify the local machine which the
    DHCP server may use to customize the DHCP lease and options. When
    the property is a hex string ('aa:bb:cc') it is interpreted as a
    binary client ID, in which case the first byte is assumed to be the
    'type' field as per RFC 2132 section 9.14 and the remaining bytes
    may be an hardware address (e.g. '01:xx:xx:xx:xx:xx:xx' where 1 is
    the Ethernet ARP type and the rest is a MAC address). If the
    property is not a hex string it is considered as a non-hardware-
    address client ID and the 'type' field is set to 0.

    The special values "mac" and "perm-mac" are supported, which use the
    current or permanent MAC address of the device to generate a client
    identifier with type ethernet (01). Currently, these options only
    work for ethernet type of links.

    The special value "ipv6-duid" uses the DUID from "ipv6.dhcp-duid"
    property as an RFC4361-compliant client identifier. As IAID it uses
    "ipv4.dhcp-iaid" and falls back to "ipv6.dhcp-iaid" if unset.

    The special value "duid" generates a RFC4361-compliant client
    identifier based on "ipv4.dhcp-iaid" and uses a DUID generated by
    hashing /etc/machine-id.

    The special value "stable" is supported to generate a type 0 client
    identifier based on the stable-id (see connection.stable-id) and a
    per-host key. If you set the stable-id, you may want to include the
    "${DEVICE}" or "${MAC}" specifier to get a per-device key.

    If unset, a globally configured default is used. If still unset, the
    default depends on the DHCP plugin."""
    dhcp_fqdn: Optional[str] = field(
        metadata={
            'dbus_name': 'dhcp-fqdn',
            'dbus_type': 's',
        },
        default=None,
    )
    """If the "dhcp-send-hostname" property is TRUE, then the specified FQDN
    will be sent to the DHCP server when acquiring a lease. This
    property and "dhcp-hostname" are mutually exclusive and cannot be
    set at the same time."""
    dhcp_hostname: Optional[str] = field(
        metadata={
            'dbus_name': 'dhcp-hostname',
            'dbus_type': 's',
        },
        default=None,
    )
    """If the "dhcp-send-hostname" property is TRUE, then the specified name
    will be sent to the DHCP server when acquiring a lease. This
    property and "dhcp-fqdn" are mutually exclusive and cannot be set at
    the same time."""
    dhcp_hostname_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'dhcp-hostname-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags for the DHCP hostname and FQDN.

    Currently, this property only includes flags to control the FQDN
    flags set in the DHCP FQDN option. Supported FQDN flags are
    NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1),
    NM_DHCP_HOSTNAME_FLAG_FQDN_ENCODED (0x2) and
    NM_DHCP_HOSTNAME_FLAG_FQDN_NO_UPDATE (0x4).  When no FQDN flag is
    set and NM_DHCP_HOSTNAME_FLAG_FQDN_CLEAR_FLAGS (0x8) is set, the
    DHCP FQDN option will contain no flag. Otherwise, if no FQDN flag is
    set and NM_DHCP_HOSTNAME_FLAG_FQDN_CLEAR_FLAGS (0x8) is not set, the
    standard FQDN flags are set in the request:
    NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1),
    NM_DHCP_HOSTNAME_FLAG_FQDN_ENCODED (0x2) for IPv4 and
    NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1) for IPv6.

    When this property is set to the default value
    NM_DHCP_HOSTNAME_FLAG_NONE (0x0), a global default is looked up in
    NetworkManager configuration. If that value is unset or also
    NM_DHCP_HOSTNAME_FLAG_NONE (0x0), then the standard FQDN flags
    described above are sent in the DHCP requests."""
    dhcp_iaid: Optional[str] = field(
        metadata={
            'dbus_name': 'dhcp-iaid',
            'dbus_type': 's',
        },
        default=None,
    )
    """A string containing the "Identity Association Identifier" (IAID) used by
    the DHCP client. The property is a 32-bit decimal value or a special
    value among "mac", "perm-mac", "ifname" and "stable". When set to
    "mac" (or "perm-mac"), the last 4 bytes of the current (or
    permanent) MAC address are used as IAID. When set to "ifname", the
    IAID is computed by hashing the interface name. The special value
    "stable" can be used to generate an IAID based on the stable-id (see
    connection.stable-id), a per-host key and the interface name. When
    the property is unset, the value from global configuration is used;
    if no global default is set then the IAID is assumed to be "ifname".
    Note that at the moment this property is ignored for IPv6 by
    dhclient, which always derives the IAID from the MAC address."""
    dhcp_reject_servers: Optional[List[str]] = field(
        metadata={
            'dbus_name': 'dhcp-reject-servers',
            'dbus_type': 'as',
        },
        default=None,
    )
    """Array of servers from which DHCP offers must be rejected. This property
    is useful to avoid getting a lease from misconfigured or rogue
    servers.

    For DHCPv4, each element must be an IPv4 address, optionally
    followed by a slash and a prefix length (e.g. "192.168.122.0/24").

    This property is currently not implemented for DHCPv6."""
    dhcp_send_hostname: Optional[bool] = field(
        metadata={
            'dbus_name': 'dhcp-send-hostname',
            'dbus_type': 'b',
        },
        default=None,
    )
    """If TRUE, a hostname is sent to the DHCP server when acquiring a lease.
    Some DHCP servers use this hostname to update DNS databases,
    essentially providing a static hostname for the computer.  If the
    "dhcp-hostname" property is NULL and this property is TRUE, the
    current persistent hostname of the computer is sent."""
    dhcp_timeout: Optional[int] = field(
        metadata={
            'dbus_name': 'dhcp-timeout',
            'dbus_type': 'i',
        },
        default=None,
    )
    """A timeout for a DHCP transaction in seconds. If zero (the default), a
    globally configured default is used. If still unspecified, a device
    specific timeout is used (usually 45 seconds).

    Set to 2147483647 (MAXINT32) for infinity."""
    dhcp_vendor_class_identifier: Optional[str] = field(
        metadata={
            'dbus_name': 'dhcp-vendor-class-identifier',
            'dbus_type': 's',
        },
        default=None,
    )
    """The Vendor Class Identifier DHCP option (60). Special characters in the
    data string may be escaped using C-style escapes, nevertheless this
    property cannot contain nul bytes. If the per-profile value is
    unspecified (the default), a global connection default gets
    consulted. If still unspecified, the DHCP option is not sent to the
    server.

    Since 1.28"""
    dns: Optional[List[int]] = field(
        metadata={
            'dbus_name': 'dns',
            'dbus_type': 'au',
        },
        default=None,
    )
    """Array of IP addresses of DNS servers.

    For DoT (DNS over TLS), the SNI server name can be specified by
    appending "#example.com" to the IP address of the DNS server. This
    currently only has effect when using systemd-resolved."""
    dns_data: Optional[List[str]] = field(
        metadata={
            'dbus_name': 'dns-data',
            'dbus_type': 'as',
        },
        default=None,
    )
    """Array of DNS name servers. This replaces the deprecated "dns" property.
    Each name server can also contain a DoT server name."""
    dns_options: Optional[List[str]] = field(
        metadata={
            'dbus_name': 'dns-options',
            'dbus_type': 'as',
        },
        default=None,
    )
    """Array of DNS options as described in man 5 resolv.conf.

    NULL means that the options are unset and left at the default. In
    this case NetworkManager will use default options. This is distinct
    from an empty list of properties.

    The currently supported options are "attempts", "debug", "edns0",
    "inet6", "ip6-bytestring", "ip6-dotint", "ndots", "no-check-names",
    "no-ip6-dotint", "no-reload", "no-tld-query", "rotate", "single-
    request", "single-request-reopen", "timeout", "trust-ad", "use-vc".

    The "trust-ad" setting is only honored if the profile contributes
    name servers to resolv.conf, and if all contributing profiles have
    "trust-ad" enabled.

    When using a caching DNS plugin (dnsmasq or systemd-resolved in
    NetworkManager.conf) then "edns0" and "trust-ad" are automatically
    added."""
    dns_priority: Optional[int] = field(
        metadata={
            'dbus_name': 'dns-priority',
            'dbus_type': 'i',
        },
        default=None,
    )
    """DNS servers priority.

    The relative priority for DNS servers specified by this setting.  A
    lower numerical value is better (higher priority).

    Negative values have the special effect of excluding other
    configurations with a greater numerical priority value; so in
    presence of at least one negative priority, only DNS servers from
    connections with the lowest priority value will be used. To avoid
    all DNS leaks, set the priority of the profile that should be used
    to the most negative value of all active connections profiles.

    Zero selects a globally configured default value. If the latter is
    missing or zero too, it defaults to 50 for VPNs (including
    WireGuard) and 100 for other connections.

    Note that the priority is to order DNS settings for multiple active
    connections.  It does not disambiguate multiple DNS servers within
    the same connection profile.

    When multiple devices have configurations with the same priority,
    VPNs will be considered first, then devices with the best (lowest
    metric) default route and then all other devices.

    When using dns=default, servers with higher priority will be on top
    of resolv.conf. To prioritize a given server over another one within
    the same connection, just specify them in the desired order. Note
    that commonly the resolver tries name servers in /etc/resolv.conf in
    the order listed, proceeding with the next server in the list on
    failure. See for example the "rotate" option of the dns-options
    setting. If there are any negative DNS priorities, then only name
    servers from the devices with that lowest priority will be
    considered.

    When using a DNS resolver that supports Conditional Forwarding or
    Split DNS (with dns=dnsmasq or dns=systemd-resolved settings), each
    connection is used to query domains in its search list. The search
    domains determine which name servers to ask, and the DNS priority is
    used to prioritize name servers based on the domain.  Queries for
    domains not present in any search list are routed through
    connections having the '~.' special wildcard domain, which is added
    automatically to connections with the default route (or can be added
    manually).  When multiple connections specify the same domain, the
    one with the best priority (lowest numerical value) wins.  If a sub
    domain is configured on another interface it will be accepted
    regardless the priority, unless parent domain on the other interface
    has a negative priority, which causes the sub domain to be shadowed.
    With Split DNS one can avoid undesired DNS leaks by properly
    configuring DNS priorities and the search domains, so that only name
    servers of the desired interface are configured."""
    dns_search: Optional[List[str]] = field(
        metadata={
            'dbus_name': 'dns-search',
            'dbus_type': 'as',
        },
        default=None,
    )
    """List of DNS search domains. Domains starting with a tilde ('~') are
    considered 'routing' domains and are used only to decide the
    interface over which a query must be forwarded; they are not used to
    complete unqualified host names.

    When using a DNS plugin that supports Conditional Forwarding or
    Split DNS, then the search domains specify which name servers to
    query. This makes the behavior different from running with plain
    /etc/resolv.conf. For more information see also the dns-priority
    setting.

    When set on a profile that also enabled DHCP, the DNS search list
    received automatically (option 119 for DHCPv4 and option 24 for
    DHCPv6) gets merged with the manual list. This can be prevented by
    setting "ignore-auto-dns". Note that if no DNS searches are
    configured, the fallback will be derived from the domain from DHCP
    (option 15)."""
    gateway: Optional[str] = field(
        metadata={
            'dbus_name': 'gateway',
            'dbus_type': 's',
        },
        default=None,
    )
    """The gateway associated with this configuration. This is only meaningful
    if "addresses" is also set.

    Setting the gateway causes NetworkManager to configure a standard
    default route with the gateway as next hop. This is ignored if
    "never-default" is set. An alternative is to configure the default
    route explicitly with a manual route and /0 as prefix length.

    Note that the gateway usually conflicts with routing that
    NetworkManager configures for WireGuard interfaces, so usually it
    should not be set in that case. See "ip4-auto-default-route"."""
    ignore_auto_dns: Optional[bool] = field(
        metadata={
            'dbus_name': 'ignore-auto-dns',
            'dbus_type': 'b',
        },
        default=None,
    )
    """When "method" is set to "auto" and this property to TRUE, automatically
    configured name servers and search domains are ignored and only name
    servers and search domains specified in the "dns" and "dns-search"
    properties, if any, are used."""
    ignore_auto_routes: Optional[bool] = field(
        metadata={
            'dbus_name': 'ignore-auto-routes',
            'dbus_type': 'b',
        },
        default=None,
    )
    """When "method" is set to "auto" and this property to TRUE, automatically
    configured routes are ignored and only routes specified in the
    "routes" property, if any, are used."""
    link_local: Optional[int] = field(
        metadata={
            'dbus_name': 'link-local',
            'dbus_type': 'i',
        },
        default=None,
    )
    """Enable and disable the IPv4 link-local configuration independently of
    the ipv4.method configuration. This allows a link-local address
    (169.254.x.y/16) to be obtained in addition to other addresses, such
    as those manually configured or obtained from a DHCP server.

    When set to "auto", the value is dependent on "ipv4.method". When
    set to "default", it honors the global connection default, before
    falling back to "auto". Note that if "ipv4.method" is "disabled",
    then link local addressing is always disabled too. The default is
    "default".

    Since 1.40"""
    may_fail: Optional[bool] = field(
        metadata={
            'dbus_name': 'may-fail',
            'dbus_type': 'b',
        },
        default=None,
    )
    """If TRUE, allow overall network configuration to proceed even if the
    configuration specified by this property times out.  Note that at
    least one IP configuration must succeed or overall network
    configuration will still fail.  For example, in IPv6-only networks,
    setting this property to TRUE on the NMSettingIP4Config allows the
    overall network configuration to succeed if IPv4 configuration fails
    but IPv6 configuration completes successfully."""
    method: Optional[str] = field(
        metadata={
            'dbus_name': 'method',
            'dbus_type': 's',
        },
        default=None,
    )
    """IP configuration method.

    NMSettingIP4Config and NMSettingIP6Config both support "disabled",
    "auto", "manual", and "link-local". See the subclass-specific
    documentation for other values.

    In general, for the "auto" method, properties such as "dns" and
    "routes" specify information that is added on to the information
    returned from automatic configuration.  The "ignore-auto-routes" and
    "ignore-auto-dns" properties modify this behavior.

    For methods that imply no upstream network, such as "shared" or
    "link-local", these properties must be empty.

    For IPv4 method "shared", the IP subnet can be configured by adding
    one manual IPv4 address or otherwise 10.42.x.0/24 is chosen. Note
    that the shared method must be configured on the interface which
    shares the internet to a subnet, not on the uplink which is shared."""
    never_default: Optional[bool] = field(
        metadata={
            'dbus_name': 'never-default',
            'dbus_type': 'b',
        },
        default=None,
    )
    """If TRUE, this connection will never be the default connection for this
    IP type, meaning it will never be assigned the default route by
    NetworkManager."""
    required_timeout: Optional[int] = field(
        metadata={
            'dbus_name': 'required-timeout',
            'dbus_type': 'i',
        },
        default=None,
    )
    """The minimum time interval in milliseconds for which dynamic IP
    configuration should be tried before the connection succeeds.

    This property is useful for example if both IPv4 and IPv6 are
    enabled and are allowed to fail. Normally the connection succeeds as
    soon as one of the two address families completes; by setting a
    required timeout for e.g. IPv4, one can ensure that even if IP6
    succeeds earlier than IPv4, NetworkManager waits some time for IPv4
    before the connection becomes active.

    Note that if "may-fail" is FALSE for the same address family, this
    property has no effect as NetworkManager needs to wait for the full
    DHCP timeout.

    A zero value means that no required timeout is present, -1 means the
    default value (either configuration ipvx.required-timeout override
    or zero)."""
    route_data: Optional[List[RouteData]] = field(
        metadata={
            'dbus_name': 'route-data',
            'dbus_type': 'aa{sv}',
            'dbus_inner_class': RouteData,
        },
        default=None,
    )
    """Array of IPv4 routes. Each route dictionary contains at least 'dest' and
    'prefix' entries, containing the destination IP address as a string,
    and the prefix length as a uint32. Most routes will also have a
    'next-hop' entry, containing the next hop IP address as a string. If
    the route has a 'metric' entry (containing a uint32), that will be
    used as the metric for the route (otherwise NM will pick a default
    value appropriate to the device). Additional attributes may also
    exist on some routes."""
    route_metric: Optional[int] = field(
        metadata={
            'dbus_name': 'route-metric',
            'dbus_type': 'x',
        },
        default=None,
    )
    """The default metric for routes that don't explicitly specify a metric.
    The default value -1 means that the metric is chosen automatically
    based on the device type. The metric applies to dynamic routes,
    manual (static) routes that don't have an explicit metric setting,
    address prefix routes, and the default route. Note that for IPv6,
    the kernel accepts zero (0) but coerces it to 1024 (user default).
    Hence, setting this property to zero effectively mean setting it to
    1024. For IPv4, zero is a regular value for the metric."""
    route_table: Optional[int] = field(
        metadata={
            'dbus_name': 'route-table',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Enable policy routing (source routing) and set the routing table used
    when adding routes.

    This affects all routes, including device-routes, IPv4LL, DHCP,
    SLAAC, default-routes and static routes. But note that static routes
    can individually overwrite the setting by explicitly specifying a
    non-zero routing table.

    If the table setting is left at zero, it is eligible to be
    overwritten via global configuration. If the property is zero even
    after applying the global configuration value, policy routing is
    disabled for the address family of this connection.

    Policy routing disabled means that NetworkManager will add all
    routes to the main table (except static routes that explicitly
    configure a different table). Additionally, NetworkManager will not
    delete any extraneous routes from tables except the main table. This
    is to preserve backward compatibility for users who manage routing
    tables outside of NetworkManager."""
    routes: Optional[List[List[int]]] = field(
        metadata={
            'dbus_name': 'routes',
            'dbus_type': 'aau',
        },
        default=None,
    )
    """Array of IP routes."""
    routing_rules: Optional[List[RoutingRules]] = field(
        metadata={
            'dbus_name': 'routing-rules',
            'dbus_type': 'aa{sv}',
            'dbus_inner_class': RoutingRules,
        },
        default=None,
    )
    """Array of dictionaries for routing rules. Each routing rule supports the
    following options: action (y), dport-end (q), dport-start (q),
    family (i), from (s), from-len (y), fwmark (u), fwmask (u), iifname
    (s), invert (b), ipproto (s), oifname (s), priority (u), sport-end
    (q), sport-start (q), supress-prefixlength (i), table (u), to (s),
    tos (y), to-len (y), range-end (u), range-start (u)."""
