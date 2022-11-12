# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses-jinja.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class EapolSettings(NetworkManagerSettingsMixin):
    """IEEE 802.1x Authentication Settings"""

    altsubject_matches: Optional[List[str]] = field(
        metadata={
            'dbus_name': 'altsubject-matches',
            'dbus_type': 'as',
        },
        default=None,
    )
    """List of strings to be matched against the altSubjectName of the
    certificate presented by the authentication server. If the list is
    empty, no verification of the server certificate's altSubjectName is
    performed."""
    anonymous_identity: Optional[str] = field(
        metadata={
            'dbus_name': 'anonymous-identity',
            'dbus_type': 's',
        },
        default=None,
    )
    """Anonymous identity string for EAP authentication methods.  Used as the
    unencrypted identity with EAP types that support different tunneled
    identity like EAP-TTLS."""
    auth_timeout: Optional[int] = field(
        metadata={
            'dbus_name': 'auth-timeout',
            'dbus_type': 'i',
        },
        default=None,
    )
    """A timeout for the authentication. Zero means the global default; if the
    global default is not set, the authentication timeout is 25 seconds."""
    ca_cert: Optional[bytes] = field(
        metadata={
            'dbus_name': 'ca-cert',
            'dbus_type': 'ay',
        },
        default=None,
    )
    """Contains the CA certificate if used by the EAP method specified in the
    "eap" property.

    Certificate data is specified using a "scheme"; three are currently
    supported: blob, path and pkcs#11 URL. When using the blob scheme
    this property should be set to the certificate's DER encoded data.
    When using the path scheme, this property should be set to the full
    UTF-8 encoded path of the certificate, prefixed with the string
    "file://" and ending with a terminating NUL byte. This property can
    be unset even if the EAP method supports CA certificates, but this
    allows man-in-the-middle attacks and is NOT recommended.

    Note that enabling NMSetting8021x:system-ca-certs will override this
    setting to use the built-in path, if the built-in path is not a
    directory."""
    ca_cert_password: Optional[str] = field(
        metadata={
            'dbus_name': 'ca-cert-password',
            'dbus_type': 's',
        },
        default=None,
    )
    """The password used to access the CA certificate stored in "ca-cert"
    property. Only makes sense if the certificate is stored on a PKCS#11
    token that requires a login."""
    ca_cert_password_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'ca-cert-password-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "ca-cert-password" property."""
    ca_path: Optional[str] = field(
        metadata={
            'dbus_name': 'ca-path',
            'dbus_type': 's',
        },
        default=None,
    )
    """UTF-8 encoded path to a directory containing PEM or DER formatted
    certificates to be added to the verification chain in addition to
    the certificate specified in the "ca-cert" property.

    If NMSetting8021x:system-ca-certs is enabled and the built-in CA
    path is an existing directory, then this setting is ignored."""
    client_cert: Optional[bytes] = field(
        metadata={
            'dbus_name': 'client-cert',
            'dbus_type': 'ay',
        },
        default=None,
    )
    """Contains the client certificate if used by the EAP method specified in
    the "eap" property.

    Certificate data is specified using a "scheme"; two are currently
    supported: blob and path. When using the blob scheme (which is
    backwards compatible with NM 0.7.x) this property should be set to
    the certificate's DER encoded data. When using the path scheme, this
    property should be set to the full UTF-8 encoded path of the
    certificate, prefixed with the string "file://" and ending with a
    terminating NUL byte."""
    client_cert_password: Optional[str] = field(
        metadata={
            'dbus_name': 'client-cert-password',
            'dbus_type': 's',
        },
        default=None,
    )
    """The password used to access the client certificate stored in "client-
    cert" property. Only makes sense if the certificate is stored on a
    PKCS#11 token that requires a login."""
    client_cert_password_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'client-cert-password-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "client-cert-password" property."""
    domain_match: Optional[str] = field(
        metadata={
            'dbus_name': 'domain-match',
            'dbus_type': 's',
        },
        default=None,
    )
    """Constraint for server domain name. If set, this list of FQDNs is used as
    a match requirement for dNSName element(s) of the certificate
    presented by the authentication server.  If a matching dNSName is
    found, this constraint is met.  If no dNSName values are present,
    this constraint is matched against SubjectName CN using the same
    comparison. Multiple valid FQDNs can be passed as a ";" delimited
    list."""
    domain_suffix_match: Optional[str] = field(
        metadata={
            'dbus_name': 'domain-suffix-match',
            'dbus_type': 's',
        },
        default=None,
    )
    """Constraint for server domain name. If set, this FQDN is used as a suffix
    match requirement for dNSName element(s) of the certificate
    presented by the authentication server.  If a matching dNSName is
    found, this constraint is met.  If no dNSName values are present,
    this constraint is matched against SubjectName CN using same suffix
    match comparison. Since version 1.24, multiple valid FQDNs can be
    passed as a ";" delimited list."""
    eap: Optional[List[str]] = field(
        metadata={
            'dbus_name': 'eap',
            'dbus_type': 'as',
        },
        default=None,
    )
    """The allowed EAP method to be used when authenticating to the network
    with 802.1x.  Valid methods are: "leap", "md5", "tls", "peap",
    "ttls", "pwd", and "fast".  Each method requires different
    configuration using the properties of this setting; refer to
    wpa_supplicant documentation for the allowed combinations."""
    identity: Optional[str] = field(
        metadata={
            'dbus_name': 'identity',
            'dbus_type': 's',
        },
        default=None,
    )
    """Identity string for EAP authentication methods.  Often the user's user
    or login name."""
    optional: Optional[bool] = field(
        metadata={
            'dbus_name': 'optional',
            'dbus_type': 'b',
        },
        default=None,
    )
    """Whether the 802.1X authentication is optional. If TRUE, the activation
    will continue even after a timeout or an authentication failure.
    Setting the property to TRUE is currently allowed only for Ethernet
    connections. If set to FALSE, the activation can continue only after
    a successful authentication."""
    pac_file: Optional[str] = field(
        metadata={
            'dbus_name': 'pac-file',
            'dbus_type': 's',
        },
        default=None,
    )
    """UTF-8 encoded file path containing PAC for EAP-FAST."""
    password: Optional[str] = field(
        metadata={
            'dbus_name': 'password',
            'dbus_type': 's',
        },
        default=None,
    )
    """UTF-8 encoded password used for EAP authentication methods. If both the
    "password" property and the "password-raw" property are specified,
    "password" is preferred."""
    password_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'password-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "password" property."""
    password_raw: Optional[bytes] = field(
        metadata={
            'dbus_name': 'password-raw',
            'dbus_type': 'ay',
        },
        default=None,
    )
    """Password used for EAP authentication methods, given as a byte array to
    allow passwords in other encodings than UTF-8 to be used. If both
    the "password" property and the "password-raw" property are
    specified, "password" is preferred."""
    password_raw_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'password-raw-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "password-raw" property."""
    phase1_auth_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'phase1-auth-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Specifies authentication flags to use in "phase 1" outer authentication
    using NMSetting8021xAuthFlags options. The individual TLS versions
    can be explicitly disabled. TLS time checks can be also disabled. If
    a certain TLS disable flag is not set, it is up to the supplicant to
    allow or forbid it. The TLS options map to tls_disable_tlsv1_x and
    tls_disable_time_checks settings. See the wpa_supplicant
    documentation for more details."""
    phase1_fast_provisioning: Optional[str] = field(
        metadata={
            'dbus_name': 'phase1-fast-provisioning',
            'dbus_type': 's',
        },
        default=None,
    )
    """Enables or disables in-line provisioning of EAP-FAST credentials when
    FAST is specified as the EAP method in the "eap" property.
    Recognized values are "0" (disabled), "1" (allow unauthenticated
    provisioning), "2" (allow authenticated provisioning), and "3"
    (allow both authenticated and unauthenticated provisioning).  See
    the wpa_supplicant documentation for more details."""
    phase1_peaplabel: Optional[str] = field(
        metadata={
            'dbus_name': 'phase1-peaplabel',
            'dbus_type': 's',
        },
        default=None,
    )
    """Forces use of the new PEAP label during key derivation.  Some RADIUS
    servers may require forcing the new PEAP label to interoperate with
    PEAPv1.  Set to "1" to force use of the new PEAP label.  See the
    wpa_supplicant documentation for more details."""
    phase1_peapver: Optional[str] = field(
        metadata={
            'dbus_name': 'phase1-peapver',
            'dbus_type': 's',
        },
        default=None,
    )
    """Forces which PEAP version is used when PEAP is set as the EAP method in
    the "eap" property.  When unset, the version reported by the server
    will be used.  Sometimes when using older RADIUS servers, it is
    necessary to force the client to use a particular PEAP version.  To
    do so, this property may be set to "0" or "1" to force that specific
    PEAP version."""
    phase2_altsubject_matches: Optional[List[str]] = field(
        metadata={
            'dbus_name': 'phase2-altsubject-matches',
            'dbus_type': 'as',
        },
        default=None,
    )
    """List of strings to be matched against the altSubjectName of the
    certificate presented by the authentication server during the inner
    "phase 2" authentication. If the list is empty, no verification of
    the server certificate's altSubjectName is performed."""
    phase2_auth: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-auth',
            'dbus_type': 's',
        },
        default=None,
    )
    """Specifies the allowed "phase 2" inner authentication method when an EAP
    method that uses an inner TLS tunnel is specified in the "eap"
    property.  For TTLS this property selects one of the supported non-
    EAP inner methods: "pap", "chap", "mschap", "mschapv2" while
    "phase2-autheap" selects an EAP inner method.  For PEAP this selects
    an inner EAP method, one of: "gtc", "otp", "md5" and "tls". Each
    "phase 2" inner method requires specific parameters for successful
    authentication; see the wpa_supplicant documentation for more
    details. Both "phase2-auth" and "phase2-autheap" cannot be
    specified."""
    phase2_autheap: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-autheap',
            'dbus_type': 's',
        },
        default=None,
    )
    """Specifies the allowed "phase 2" inner EAP-based authentication method
    when TTLS is specified in the "eap" property.  Recognized EAP-based
    "phase 2" methods are "md5", "mschapv2", "otp", "gtc", and "tls".
    Each "phase 2" inner method requires specific parameters for
    successful authentication; see the wpa_supplicant documentation for
    more details."""
    phase2_ca_cert: Optional[bytes] = field(
        metadata={
            'dbus_name': 'phase2-ca-cert',
            'dbus_type': 'ay',
        },
        default=None,
    )
    """Contains the "phase 2" CA certificate if used by the EAP method
    specified in the "phase2-auth" or "phase2-autheap" properties.

    Certificate data is specified using a "scheme"; three are currently
    supported: blob, path and pkcs#11 URL. When using the blob scheme
    this property should be set to the certificate's DER encoded data.
    When using the path scheme, this property should be set to the full
    UTF-8 encoded path of the certificate, prefixed with the string
    "file://" and ending with a terminating NUL byte. This property can
    be unset even if the EAP method supports CA certificates, but this
    allows man-in-the-middle attacks and is NOT recommended.

    Note that enabling NMSetting8021x:system-ca-certs will override this
    setting to use the built-in path, if the built-in path is not a
    directory."""
    phase2_ca_cert_password: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-ca-cert-password',
            'dbus_type': 's',
        },
        default=None,
    )
    """The password used to access the "phase2" CA certificate stored in
    "phase2-ca-cert" property. Only makes sense if the certificate is
    stored on a PKCS#11 token that requires a login."""
    phase2_ca_cert_password_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'phase2-ca-cert-password-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "phase2-ca-cert-password" property."""
    phase2_ca_path: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-ca-path',
            'dbus_type': 's',
        },
        default=None,
    )
    """UTF-8 encoded path to a directory containing PEM or DER formatted
    certificates to be added to the verification chain in addition to
    the certificate specified in the "phase2-ca-cert" property.

    If NMSetting8021x:system-ca-certs is enabled and the built-in CA
    path is an existing directory, then this setting is ignored."""
    phase2_client_cert: Optional[bytes] = field(
        metadata={
            'dbus_name': 'phase2-client-cert',
            'dbus_type': 'ay',
        },
        default=None,
    )
    """Contains the "phase 2" client certificate if used by the EAP method
    specified in the "phase2-auth" or "phase2-autheap" properties.

    Certificate data is specified using a "scheme"; two are currently
    supported: blob and path. When using the blob scheme (which is
    backwards compatible with NM 0.7.x) this property should be set to
    the certificate's DER encoded data. When using the path scheme, this
    property should be set to the full UTF-8 encoded path of the
    certificate, prefixed with the string "file://" and ending with a
    terminating NUL byte. This property can be unset even if the EAP
    method supports CA certificates, but this allows man-in-the-middle
    attacks and is NOT recommended."""
    phase2_client_cert_password: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-client-cert-password',
            'dbus_type': 's',
        },
        default=None,
    )
    """The password used to access the "phase2" client certificate stored in
    "phase2-client-cert" property. Only makes sense if the certificate
    is stored on a PKCS#11 token that requires a login."""
    phase2_client_cert_password_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'phase2-client-cert-password-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "phase2-client-cert-password"
    property."""
    phase2_domain_match: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-domain-match',
            'dbus_type': 's',
        },
        default=None,
    )
    """Constraint for server domain name. If set, this list of FQDNs is used as
    a match requirement for dNSName element(s) of the certificate
    presented by the authentication server during the inner "phase 2"
    authentication. If a matching dNSName is found, this constraint is
    met.  If no dNSName values are present, this constraint is matched
    against SubjectName CN using the same comparison. Multiple valid
    FQDNs can be passed as a ";" delimited list."""
    phase2_domain_suffix_match: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-domain-suffix-match',
            'dbus_type': 's',
        },
        default=None,
    )
    """Constraint for server domain name. If set, this FQDN is used as a suffix
    match requirement for dNSName element(s) of the certificate
    presented by the authentication server during the inner "phase 2"
    authentication.  If a matching dNSName is found, this constraint is
    met.  If no dNSName values are present, this constraint is matched
    against SubjectName CN using same suffix match comparison. Since
    version 1.24, multiple valid FQDNs can be passed as a ";" delimited
    list."""
    phase2_private_key: Optional[bytes] = field(
        metadata={
            'dbus_name': 'phase2-private-key',
            'dbus_type': 'ay',
        },
        default=None,
    )
    """Contains the "phase 2" inner private key when the "phase2-auth" or
    "phase2-autheap" property is set to "tls".

    Key data is specified using a "scheme"; two are currently supported:
    blob and path. When using the blob scheme and private keys, this
    property should be set to the key's encrypted PEM encoded data. When
    using private keys with the path scheme, this property should be set
    to the full UTF-8 encoded path of the key, prefixed with the string
    "file://" and ending with a terminating NUL byte. When using PKCS#12
    format private keys and the blob scheme, this property should be set
    to the PKCS#12 data and the "phase2-private-key-password" property
    must be set to password used to decrypt the PKCS#12 certificate and
    key. When using PKCS#12 files and the path scheme, this property
    should be set to the full UTF-8 encoded path of the key, prefixed
    with the string "file://" and ending with a terminating NUL byte,
    and as with the blob scheme the "phase2-private-key-password"
    property must be set to the password used to decode the PKCS#12
    private key and certificate."""
    phase2_private_key_password: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-private-key-password',
            'dbus_type': 's',
        },
        default=None,
    )
    """The password used to decrypt the "phase 2" private key specified in the
    "phase2-private-key" property when the private key either uses the
    path scheme, or is a PKCS#12 format key."""
    phase2_private_key_password_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'phase2-private-key-password-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "phase2-private-key-password"
    property."""
    phase2_subject_match: Optional[str] = field(
        metadata={
            'dbus_name': 'phase2-subject-match',
            'dbus_type': 's',
        },
        default=None,
    )
    """Substring to be matched against the subject of the certificate presented
    by the authentication server during the inner "phase 2"
    authentication. When unset, no verification of the authentication
    server certificate's subject is performed. This property provides
    little security, if any, and should not be used."""
    pin: Optional[str] = field(
        metadata={
            'dbus_name': 'pin',
            'dbus_type': 's',
        },
        default=None,
    )
    """PIN used for EAP authentication methods."""
    pin_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'pin-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "pin" property."""
    private_key: Optional[bytes] = field(
        metadata={
            'dbus_name': 'private-key',
            'dbus_type': 'ay',
        },
        default=None,
    )
    """Contains the private key when the "eap" property is set to "tls".

    Key data is specified using a "scheme"; two are currently supported:
    blob and path. When using the blob scheme and private keys, this
    property should be set to the key's encrypted PEM encoded data. When
    using private keys with the path scheme, this property should be set
    to the full UTF-8 encoded path of the key, prefixed with the string
    "file://" and ending with a terminating NUL byte. When using PKCS#12
    format private keys and the blob scheme, this property should be set
    to the PKCS#12 data and the "private-key-password" property must be
    set to password used to decrypt the PKCS#12 certificate and key.
    When using PKCS#12 files and the path scheme, this property should
    be set to the full UTF-8 encoded path of the key, prefixed with the
    string "file://" and ending with a terminating NUL byte, and as with
    the blob scheme the "private-key-password" property must be set to
    the password used to decode the PKCS#12 private key and certificate.

    WARNING: "private-key" is not a "secret" property, and thus
    unencrypted private key data using the BLOB scheme may be readable
    by unprivileged users.  Private keys should always be encrypted with
    a private key password to prevent unauthorized access to unencrypted
    private key data."""
    private_key_password: Optional[str] = field(
        metadata={
            'dbus_name': 'private-key-password',
            'dbus_type': 's',
        },
        default=None,
    )
    """The password used to decrypt the private key specified in the "private-
    key" property when the private key either uses the path scheme, or
    if the private key is a PKCS#12 format key."""
    private_key_password_flags: Optional[int] = field(
        metadata={
            'dbus_name': 'private-key-password-flags',
            'dbus_type': 'u',
        },
        default=None,
    )
    """Flags indicating how to handle the "private-key-password" property."""
    subject_match: Optional[str] = field(
        metadata={
            'dbus_name': 'subject-match',
            'dbus_type': 's',
        },
        default=None,
    )
    """Substring to be matched against the subject of the certificate presented
    by the authentication server. When unset, no verification of the
    authentication server certificate's subject is performed. This
    property provides little security, if any, and should not be used."""
    system_ca_certs: Optional[bool] = field(
        metadata={
            'dbus_name': 'system-ca-certs',
            'dbus_type': 'b',
        },
        default=None,
    )
    """When TRUE, overrides the "ca-path" and "phase2-ca-path" properties using
    the system CA directory specified at configure time with the
    --system-ca-path switch.  The certificates in this directory are
    added to the verification chain in addition to any certificates
    specified by the "ca-cert" and "phase2-ca-cert" properties. If the
    path provided with --system-ca-path is rather a file name (bundle of
    trusted CA certificates), it overrides "ca-cert" and "phase2-ca-
    cert" properties instead (sets ca_cert/ca_cert2 options for
    wpa_supplicant)."""
