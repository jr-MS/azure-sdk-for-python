# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class ArcSettingAggregateState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Aggregate state of Arc agent across the nodes in this HCI cluster.
    """

    NOT_SPECIFIED = "NotSpecified"
    ERROR = "Error"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    DELETED = "Deleted"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    MOVING = "Moving"
    PARTIALLY_SUCCEEDED = "PartiallySucceeded"
    PARTIALLY_CONNECTED = "PartiallyConnected"
    IN_PROGRESS = "InProgress"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DiagnosticLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Desired level of diagnostic data emitted by the cluster.
    """

    OFF = "Off"
    BASIC = "Basic"
    ENHANCED = "Enhanced"

class ExtensionAggregateState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Aggregate state of Arc Extensions across the nodes in this HCI cluster.
    """

    NOT_SPECIFIED = "NotSpecified"
    ERROR = "Error"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    DELETED = "Deleted"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    MOVING = "Moving"
    PARTIALLY_SUCCEEDED = "PartiallySucceeded"
    PARTIALLY_CONNECTED = "PartiallyConnected"
    IN_PROGRESS = "InProgress"

class ImdsAttestation(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """IMDS attestation status of the cluster.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class NodeArcState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of Arc agent in this node.
    """

    NOT_SPECIFIED = "NotSpecified"
    ERROR = "Error"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    DELETED = "Deleted"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    MOVING = "Moving"

class NodeExtensionState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of Arc Extension in this node.
    """

    NOT_SPECIFIED = "NotSpecified"
    ERROR = "Error"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    DELETED = "Deleted"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    MOVING = "Moving"

class Origin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the ArcSetting proxy resource.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    ACCEPTED = "Accepted"
    PROVISIONING = "Provisioning"

class Status(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the cluster agent.
    """

    NOT_YET_REGISTERED = "NotYetRegistered"
    CONNECTED_RECENTLY = "ConnectedRecently"
    NOT_CONNECTED_RECENTLY = "NotConnectedRecently"
    DISCONNECTED = "Disconnected"
    ERROR = "Error"

class WindowsServerSubscription(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Desired state of Windows Server Subscription.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"
