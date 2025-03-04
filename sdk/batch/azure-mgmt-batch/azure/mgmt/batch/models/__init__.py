# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ActivateApplicationPackageParameters
from ._models_py3 import Application
from ._models_py3 import ApplicationPackage
from ._models_py3 import ApplicationPackageReference
from ._models_py3 import AutoScaleRun
from ._models_py3 import AutoScaleRunError
from ._models_py3 import AutoScaleSettings
from ._models_py3 import AutoStorageBaseProperties
from ._models_py3 import AutoStorageProperties
from ._models_py3 import AutoUserSpecification
from ._models_py3 import AzureBlobFileSystemConfiguration
from ._models_py3 import AzureFileShareConfiguration
from ._models_py3 import BatchAccount
from ._models_py3 import BatchAccountCreateParameters
from ._models_py3 import BatchAccountIdentity
from ._models_py3 import BatchAccountKeys
from ._models_py3 import BatchAccountListResult
from ._models_py3 import BatchAccountRegenerateKeyParameters
from ._models_py3 import BatchAccountUpdateParameters
from ._models_py3 import BatchLocationQuota
from ._models_py3 import BatchPoolIdentity
from ._models_py3 import CIFSMountConfiguration
from ._models_py3 import Certificate
from ._models_py3 import CertificateBaseProperties
from ._models_py3 import CertificateCreateOrUpdateParameters
from ._models_py3 import CertificateCreateOrUpdateProperties
from ._models_py3 import CertificateProperties
from ._models_py3 import CertificateReference
from ._models_py3 import CheckNameAvailabilityParameters
from ._models_py3 import CheckNameAvailabilityResult
from ._models_py3 import CloudErrorBody
from ._models_py3 import CloudServiceConfiguration
from ._models_py3 import ComputeNodeIdentityReference
from ._models_py3 import ContainerConfiguration
from ._models_py3 import ContainerRegistry
from ._models_py3 import DataDisk
from ._models_py3 import DeleteCertificateError
from ._models_py3 import DeploymentConfiguration
from ._models_py3 import DetectorListResult
from ._models_py3 import DetectorResponse
from ._models_py3 import DiffDiskSettings
from ._models_py3 import DiskEncryptionConfiguration
from ._models_py3 import EncryptionProperties
from ._models_py3 import EndpointAccessProfile
from ._models_py3 import EndpointDependency
from ._models_py3 import EndpointDetail
from ._models_py3 import EnvironmentSetting
from ._models_py3 import FixedScaleSettings
from ._models_py3 import IPRule
from ._models_py3 import ImageReference
from ._models_py3 import InboundNatPool
from ._models_py3 import KeyVaultProperties
from ._models_py3 import KeyVaultReference
from ._models_py3 import LinuxUserConfiguration
from ._models_py3 import ListApplicationPackagesResult
from ._models_py3 import ListApplicationsResult
from ._models_py3 import ListCertificatesResult
from ._models_py3 import ListPoolsResult
from ._models_py3 import ListPrivateEndpointConnectionsResult
from ._models_py3 import ListPrivateLinkResourcesResult
from ._models_py3 import MetadataItem
from ._models_py3 import MountConfiguration
from ._models_py3 import NFSMountConfiguration
from ._models_py3 import NetworkConfiguration
from ._models_py3 import NetworkProfile
from ._models_py3 import NetworkSecurityGroupRule
from ._models_py3 import NodePlacementConfiguration
from ._models_py3 import OSDisk
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OutboundEnvironmentEndpoint
from ._models_py3 import OutboundEnvironmentEndpointCollection
from ._models_py3 import Pool
from ._models_py3 import PoolEndpointConfiguration
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import PublicIPAddressConfiguration
from ._models_py3 import ResizeError
from ._models_py3 import ResizeOperationStatus
from ._models_py3 import Resource
from ._models_py3 import ResourceFile
from ._models_py3 import ScaleSettings
from ._models_py3 import SkuCapability
from ._models_py3 import StartTask
from ._models_py3 import SupportedSku
from ._models_py3 import SupportedSkusResult
from ._models_py3 import TaskContainerSettings
from ._models_py3 import TaskSchedulingPolicy
from ._models_py3 import UserAccount
from ._models_py3 import UserAssignedIdentities
from ._models_py3 import UserIdentity
from ._models_py3 import VMExtension
from ._models_py3 import VirtualMachineConfiguration
from ._models_py3 import VirtualMachineFamilyCoreQuota
from ._models_py3 import WindowsConfiguration
from ._models_py3 import WindowsUserConfiguration


from ._batch_management_client_enums import (
    AccountKeyType,
    AllocationState,
    AuthenticationMode,
    AutoStorageAuthenticationMode,
    AutoUserScope,
    CachingType,
    CertificateFormat,
    CertificateProvisioningState,
    CertificateStoreLocation,
    CertificateVisibility,
    ComputeNodeDeallocationOption,
    ComputeNodeFillType,
    ContainerWorkingDirectory,
    DiskEncryptionTarget,
    DynamicVNetAssignmentScope,
    ElevationLevel,
    EndpointAccessDefaultAction,
    IPAddressProvisioningType,
    InboundEndpointProtocol,
    InterNodeCommunicationState,
    KeySource,
    LoginMode,
    NameAvailabilityReason,
    NetworkSecurityGroupRuleAccess,
    NodePlacementPolicyType,
    PackageState,
    PoolAllocationMode,
    PoolIdentityType,
    PoolProvisioningState,
    PrivateEndpointConnectionProvisioningState,
    PrivateLinkServiceConnectionStatus,
    ProvisioningState,
    PublicNetworkAccessType,
    ResourceIdentityType,
    StorageAccountType,
)

__all__ = [
    'ActivateApplicationPackageParameters',
    'Application',
    'ApplicationPackage',
    'ApplicationPackageReference',
    'AutoScaleRun',
    'AutoScaleRunError',
    'AutoScaleSettings',
    'AutoStorageBaseProperties',
    'AutoStorageProperties',
    'AutoUserSpecification',
    'AzureBlobFileSystemConfiguration',
    'AzureFileShareConfiguration',
    'BatchAccount',
    'BatchAccountCreateParameters',
    'BatchAccountIdentity',
    'BatchAccountKeys',
    'BatchAccountListResult',
    'BatchAccountRegenerateKeyParameters',
    'BatchAccountUpdateParameters',
    'BatchLocationQuota',
    'BatchPoolIdentity',
    'CIFSMountConfiguration',
    'Certificate',
    'CertificateBaseProperties',
    'CertificateCreateOrUpdateParameters',
    'CertificateCreateOrUpdateProperties',
    'CertificateProperties',
    'CertificateReference',
    'CheckNameAvailabilityParameters',
    'CheckNameAvailabilityResult',
    'CloudErrorBody',
    'CloudServiceConfiguration',
    'ComputeNodeIdentityReference',
    'ContainerConfiguration',
    'ContainerRegistry',
    'DataDisk',
    'DeleteCertificateError',
    'DeploymentConfiguration',
    'DetectorListResult',
    'DetectorResponse',
    'DiffDiskSettings',
    'DiskEncryptionConfiguration',
    'EncryptionProperties',
    'EndpointAccessProfile',
    'EndpointDependency',
    'EndpointDetail',
    'EnvironmentSetting',
    'FixedScaleSettings',
    'IPRule',
    'ImageReference',
    'InboundNatPool',
    'KeyVaultProperties',
    'KeyVaultReference',
    'LinuxUserConfiguration',
    'ListApplicationPackagesResult',
    'ListApplicationsResult',
    'ListCertificatesResult',
    'ListPoolsResult',
    'ListPrivateEndpointConnectionsResult',
    'ListPrivateLinkResourcesResult',
    'MetadataItem',
    'MountConfiguration',
    'NFSMountConfiguration',
    'NetworkConfiguration',
    'NetworkProfile',
    'NetworkSecurityGroupRule',
    'NodePlacementConfiguration',
    'OSDisk',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'OutboundEnvironmentEndpoint',
    'OutboundEnvironmentEndpointCollection',
    'Pool',
    'PoolEndpointConfiguration',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateLinkResource',
    'PrivateLinkServiceConnectionState',
    'ProxyResource',
    'PublicIPAddressConfiguration',
    'ResizeError',
    'ResizeOperationStatus',
    'Resource',
    'ResourceFile',
    'ScaleSettings',
    'SkuCapability',
    'StartTask',
    'SupportedSku',
    'SupportedSkusResult',
    'TaskContainerSettings',
    'TaskSchedulingPolicy',
    'UserAccount',
    'UserAssignedIdentities',
    'UserIdentity',
    'VMExtension',
    'VirtualMachineConfiguration',
    'VirtualMachineFamilyCoreQuota',
    'WindowsConfiguration',
    'WindowsUserConfiguration',
    'AccountKeyType',
    'AllocationState',
    'AuthenticationMode',
    'AutoStorageAuthenticationMode',
    'AutoUserScope',
    'CachingType',
    'CertificateFormat',
    'CertificateProvisioningState',
    'CertificateStoreLocation',
    'CertificateVisibility',
    'ComputeNodeDeallocationOption',
    'ComputeNodeFillType',
    'ContainerWorkingDirectory',
    'DiskEncryptionTarget',
    'DynamicVNetAssignmentScope',
    'ElevationLevel',
    'EndpointAccessDefaultAction',
    'IPAddressProvisioningType',
    'InboundEndpointProtocol',
    'InterNodeCommunicationState',
    'KeySource',
    'LoginMode',
    'NameAvailabilityReason',
    'NetworkSecurityGroupRuleAccess',
    'NodePlacementPolicyType',
    'PackageState',
    'PoolAllocationMode',
    'PoolIdentityType',
    'PoolProvisioningState',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateLinkServiceConnectionStatus',
    'ProvisioningState',
    'PublicNetworkAccessType',
    'ResourceIdentityType',
    'StorageAccountType',
]
