# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class KnownColumnDefinitionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the column data."""

    STRING = "string"
    INT = "int"
    LONG = "long"
    REAL = "real"
    BOOLEAN = "boolean"
    DATETIME = "datetime"
    DYNAMIC = "dynamic"


class KnownDataCollectionEndpointProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The resource provisioning state. This property is READ-ONLY."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class KnownDataCollectionEndpointResourceKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of the resource."""

    LINUX = "Linux"
    WINDOWS = "Windows"


class KnownDataCollectionRuleAssociationProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The resource provisioning state."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class KnownDataCollectionRuleProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The resource provisioning state."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class KnownDataCollectionRuleResourceKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of the resource."""

    LINUX = "Linux"
    WINDOWS = "Windows"


class KnownDataFlowStreams(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """KnownDataFlowStreams."""

    MICROSOFT_EVENT = "Microsoft-Event"
    MICROSOFT_INSIGHTS_METRICS = "Microsoft-InsightsMetrics"
    MICROSOFT_PERF = "Microsoft-Perf"
    MICROSOFT_SYSLOG = "Microsoft-Syslog"
    MICROSOFT_WINDOWS_EVENT = "Microsoft-WindowsEvent"


class KnownExtensionDataSourceStreams(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """KnownExtensionDataSourceStreams."""

    MICROSOFT_EVENT = "Microsoft-Event"
    MICROSOFT_INSIGHTS_METRICS = "Microsoft-InsightsMetrics"
    MICROSOFT_PERF = "Microsoft-Perf"
    MICROSOFT_SYSLOG = "Microsoft-Syslog"
    MICROSOFT_WINDOWS_EVENT = "Microsoft-WindowsEvent"


class KnownLogFilesDataSourceFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The data format of the log files."""

    TEXT = "text"


class KnownLogFileTextSettingsRecordStartTimestampFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """One of the supported timestamp formats."""

    ISO8601 = "ISO 8601"
    YYYY_MM_DD_HH_MM_SS = "YYYY-MM-DD HH:MM:SS"
    M_D_YYYY_HH_MM_SS_AM_PM = "M/D/YYYY HH:MM:SS AM/PM"
    MON_DD_YYYY_HH_MM_SS = "Mon DD, YYYY HH:MM:SS"
    YY_M_MDD_HH_MM_SS = "yyMMdd HH:mm:ss"
    DD_M_MYY_HH_MM_SS = "ddMMyy HH:mm:ss"
    MMM_D_HH_MM_SS = "MMM d hh:mm:ss"
    DD_MMM_YYYY_HH_MM_SS_ZZZ = "dd/MMM/yyyy:HH:mm:ss zzz"
    YYYY_MM_DD_THH_MM_SS_K = "yyyy-MM-ddTHH:mm:ssK"


class KnownPerfCounterDataSourceStreams(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """KnownPerfCounterDataSourceStreams."""

    MICROSOFT_PERF = "Microsoft-Perf"
    MICROSOFT_INSIGHTS_METRICS = "Microsoft-InsightsMetrics"


class KnownPublicNetworkAccessOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The configuration to set whether network access from public internet to the endpoints are
    allowed.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class KnownSyslogDataSourceFacilityNames(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """KnownSyslogDataSourceFacilityNames."""

    AUTH = "auth"
    AUTHPRIV = "authpriv"
    CRON = "cron"
    DAEMON = "daemon"
    KERN = "kern"
    LPR = "lpr"
    MAIL = "mail"
    MARK = "mark"
    NEWS = "news"
    SYSLOG = "syslog"
    USER = "user"
    UUCP = "uucp"
    LOCAL0 = "local0"
    LOCAL1 = "local1"
    LOCAL2 = "local2"
    LOCAL3 = "local3"
    LOCAL4 = "local4"
    LOCAL5 = "local5"
    LOCAL6 = "local6"
    LOCAL7 = "local7"
    ASTERISK = "*"


class KnownSyslogDataSourceLogLevels(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """KnownSyslogDataSourceLogLevels."""

    DEBUG = "Debug"
    INFO = "Info"
    NOTICE = "Notice"
    WARNING = "Warning"
    ERROR = "Error"
    CRITICAL = "Critical"
    ALERT = "Alert"
    EMERGENCY = "Emergency"
    ASTERISK = "*"


class KnownSyslogDataSourceStreams(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """KnownSyslogDataSourceStreams."""

    MICROSOFT_SYSLOG = "Microsoft-Syslog"


class KnownWindowsEventLogDataSourceStreams(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """KnownWindowsEventLogDataSourceStreams."""

    MICROSOFT_WINDOWS_EVENT = "Microsoft-WindowsEvent"
    MICROSOFT_EVENT = "Microsoft-Event"
