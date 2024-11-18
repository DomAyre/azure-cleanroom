# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessPolicy
    from ._models_py3 import AccountImmutabilityPolicyProperties
    from ._models_py3 import AccountSasParameters
    from ._models_py3 import ActiveDirectoryProperties
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import AzureFilesIdentityBasedAuthentication
    from ._models_py3 import BlobContainer
    from ._models_py3 import BlobInventoryCreationTime
    from ._models_py3 import BlobInventoryPolicy
    from ._models_py3 import BlobInventoryPolicyDefinition
    from ._models_py3 import BlobInventoryPolicyFilter
    from ._models_py3 import BlobInventoryPolicyRule
    from ._models_py3 import BlobInventoryPolicySchema
    from ._models_py3 import BlobRestoreParameters
    from ._models_py3 import BlobRestoreRange
    from ._models_py3 import BlobRestoreStatus
    from ._models_py3 import BlobServiceItems
    from ._models_py3 import BlobServiceProperties
    from ._models_py3 import ChangeFeed
    from ._models_py3 import CheckNameAvailabilityResult
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import CorsRule
    from ._models_py3 import CorsRules
    from ._models_py3 import CustomDomain
    from ._models_py3 import DateAfterCreation
    from ._models_py3 import DateAfterModification
    from ._models_py3 import DeleteRetentionPolicy
    from ._models_py3 import DeletedAccount
    from ._models_py3 import DeletedAccountListResult
    from ._models_py3 import DeletedShare
    from ._models_py3 import Dimension
    from ._models_py3 import Encryption
    from ._models_py3 import EncryptionIdentity
    from ._models_py3 import EncryptionScope
    from ._models_py3 import EncryptionScopeKeyVaultProperties
    from ._models_py3 import EncryptionScopeListResult
    from ._models_py3 import EncryptionService
    from ._models_py3 import EncryptionServices
    from ._models_py3 import Endpoints
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ErrorResponseAutoGenerated
    from ._models_py3 import ErrorResponseBody
    from ._models_py3 import ExecutionTarget
    from ._models_py3 import ExecutionTargetUpdate
    from ._models_py3 import ExecutionTrigger
    from ._models_py3 import ExecutionTriggerUpdate
    from ._models_py3 import ExtendedLocation
    from ._models_py3 import FileServiceItems
    from ._models_py3 import FileServiceProperties
    from ._models_py3 import FileShare
    from ._models_py3 import FileShareItem
    from ._models_py3 import FileShareItems
    from ._models_py3 import GeoReplicationStats
    from ._models_py3 import IPRule
    from ._models_py3 import Identity
    from ._models_py3 import ImmutabilityPolicy
    from ._models_py3 import ImmutabilityPolicyProperties
    from ._models_py3 import ImmutableStorageAccount
    from ._models_py3 import ImmutableStorageWithVersioning
    from ._models_py3 import KeyCreationTime
    from ._models_py3 import KeyPolicy
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import LastAccessTimeTrackingPolicy
    from ._models_py3 import LeaseContainerRequest
    from ._models_py3 import LeaseContainerResponse
    from ._models_py3 import LeaseShareRequest
    from ._models_py3 import LeaseShareResponse
    from ._models_py3 import LegalHold
    from ._models_py3 import LegalHoldProperties
    from ._models_py3 import ListAccountSasResponse
    from ._models_py3 import ListBlobInventoryPolicy
    from ._models_py3 import ListContainerItem
    from ._models_py3 import ListContainerItems
    from ._models_py3 import ListQueue
    from ._models_py3 import ListQueueResource
    from ._models_py3 import ListQueueServices
    from ._models_py3 import ListServiceSasResponse
    from ._models_py3 import ListTableResource
    from ._models_py3 import ListTableServices
    from ._models_py3 import LocalUser
    from ._models_py3 import LocalUserKeys
    from ._models_py3 import LocalUserRegeneratePasswordResult
    from ._models_py3 import LocalUsers
    from ._models_py3 import ManagementPolicy
    from ._models_py3 import ManagementPolicyAction
    from ._models_py3 import ManagementPolicyBaseBlob
    from ._models_py3 import ManagementPolicyDefinition
    from ._models_py3 import ManagementPolicyFilter
    from ._models_py3 import ManagementPolicyRule
    from ._models_py3 import ManagementPolicySchema
    from ._models_py3 import ManagementPolicySnapShot
    from ._models_py3 import ManagementPolicyVersion
    from ._models_py3 import MetricSpecification
    from ._models_py3 import Multichannel
    from ._models_py3 import NetworkRuleSet
    from ._models_py3 import NetworkSecurityPerimeter
    from ._models_py3 import NetworkSecurityPerimeterConfiguration
    from ._models_py3 import NetworkSecurityPerimeterConfigurationList
    from ._models_py3 import NetworkSecurityPerimeterConfigurationPropertiesProfile
    from ._models_py3 import NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation
    from ._models_py3 import NspAccessRule
    from ._models_py3 import NspAccessRuleProperties
    from ._models_py3 import NspAccessRulePropertiesSubscriptionsItem
    from ._models_py3 import ObjectReplicationPolicies
    from ._models_py3 import ObjectReplicationPolicy
    from ._models_py3 import ObjectReplicationPolicyFilter
    from ._models_py3 import ObjectReplicationPolicyRule
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PermissionScope
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProtectedAppendWritesHistory
    from ._models_py3 import ProtocolSettings
    from ._models_py3 import ProvisioningIssue
    from ._models_py3 import ProvisioningIssueProperties
    from ._models_py3 import ProxyResource
    from ._models_py3 import ProxyResourceAutoGenerated
    from ._models_py3 import QueueServiceProperties
    from ._models_py3 import Resource
    from ._models_py3 import ResourceAccessRule
    from ._models_py3 import ResourceAutoGenerated
    from ._models_py3 import RestorePolicyProperties
    from ._models_py3 import Restriction
    from ._models_py3 import RoutingPreference
    from ._models_py3 import SKUCapability
    from ._models_py3 import SasPolicy
    from ._models_py3 import ServiceSasParameters
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import SignedIdentifier
    from ._models_py3 import Sku
    from ._models_py3 import SkuInformation
    from ._models_py3 import SmbSetting
    from ._models_py3 import SshPublicKey
    from ._models_py3 import StorageAccount
    from ._models_py3 import StorageAccountCheckNameAvailabilityParameters
    from ._models_py3 import StorageAccountCreateParameters
    from ._models_py3 import StorageAccountInternetEndpoints
    from ._models_py3 import StorageAccountKey
    from ._models_py3 import StorageAccountListKeysResult
    from ._models_py3 import StorageAccountListResult
    from ._models_py3 import StorageAccountMicrosoftEndpoints
    from ._models_py3 import StorageAccountMigration
    from ._models_py3 import StorageAccountRegenerateKeyParameters
    from ._models_py3 import StorageAccountSkuConversionStatus
    from ._models_py3 import StorageAccountUpdateParameters
    from ._models_py3 import StorageQueue
    from ._models_py3 import StorageSkuListResult
    from ._models_py3 import StorageTaskAssignment
    from ._models_py3 import StorageTaskAssignmentExecutionContext
    from ._models_py3 import StorageTaskAssignmentProperties
    from ._models_py3 import StorageTaskAssignmentReport
    from ._models_py3 import StorageTaskAssignmentUpdateExecutionContext
    from ._models_py3 import StorageTaskAssignmentUpdateParameters
    from ._models_py3 import StorageTaskAssignmentUpdateProperties
    from ._models_py3 import StorageTaskAssignmentUpdateReport
    from ._models_py3 import StorageTaskAssignmentsList
    from ._models_py3 import StorageTaskReportInstance
    from ._models_py3 import StorageTaskReportProperties
    from ._models_py3 import StorageTaskReportSummary
    from ._models_py3 import SystemData
    from ._models_py3 import Table
    from ._models_py3 import TableAccessPolicy
    from ._models_py3 import TableServiceProperties
    from ._models_py3 import TableSignedIdentifier
    from ._models_py3 import TagFilter
    from ._models_py3 import TagProperty
    from ._models_py3 import TrackedResource
    from ._models_py3 import TriggerParameters
    from ._models_py3 import TriggerParametersUpdate
    from ._models_py3 import UpdateHistoryProperty
    from ._models_py3 import Usage
    from ._models_py3 import UsageListResult
    from ._models_py3 import UsageName
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import VirtualNetworkRule
except (SyntaxError, ImportError):
    from ._models import AccessPolicy  # type: ignore
    from ._models import AccountImmutabilityPolicyProperties  # type: ignore
    from ._models import AccountSasParameters  # type: ignore
    from ._models import ActiveDirectoryProperties  # type: ignore
    from ._models import AzureEntityResource  # type: ignore
    from ._models import AzureFilesIdentityBasedAuthentication  # type: ignore
    from ._models import BlobContainer  # type: ignore
    from ._models import BlobInventoryCreationTime  # type: ignore
    from ._models import BlobInventoryPolicy  # type: ignore
    from ._models import BlobInventoryPolicyDefinition  # type: ignore
    from ._models import BlobInventoryPolicyFilter  # type: ignore
    from ._models import BlobInventoryPolicyRule  # type: ignore
    from ._models import BlobInventoryPolicySchema  # type: ignore
    from ._models import BlobRestoreParameters  # type: ignore
    from ._models import BlobRestoreRange  # type: ignore
    from ._models import BlobRestoreStatus  # type: ignore
    from ._models import BlobServiceItems  # type: ignore
    from ._models import BlobServiceProperties  # type: ignore
    from ._models import ChangeFeed  # type: ignore
    from ._models import CheckNameAvailabilityResult  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import CorsRule  # type: ignore
    from ._models import CorsRules  # type: ignore
    from ._models import CustomDomain  # type: ignore
    from ._models import DateAfterCreation  # type: ignore
    from ._models import DateAfterModification  # type: ignore
    from ._models import DeleteRetentionPolicy  # type: ignore
    from ._models import DeletedAccount  # type: ignore
    from ._models import DeletedAccountListResult  # type: ignore
    from ._models import DeletedShare  # type: ignore
    from ._models import Dimension  # type: ignore
    from ._models import Encryption  # type: ignore
    from ._models import EncryptionIdentity  # type: ignore
    from ._models import EncryptionScope  # type: ignore
    from ._models import EncryptionScopeKeyVaultProperties  # type: ignore
    from ._models import EncryptionScopeListResult  # type: ignore
    from ._models import EncryptionService  # type: ignore
    from ._models import EncryptionServices  # type: ignore
    from ._models import Endpoints  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ErrorResponseAutoGenerated  # type: ignore
    from ._models import ErrorResponseBody  # type: ignore
    from ._models import ExecutionTarget  # type: ignore
    from ._models import ExecutionTargetUpdate  # type: ignore
    from ._models import ExecutionTrigger  # type: ignore
    from ._models import ExecutionTriggerUpdate  # type: ignore
    from ._models import ExtendedLocation  # type: ignore
    from ._models import FileServiceItems  # type: ignore
    from ._models import FileServiceProperties  # type: ignore
    from ._models import FileShare  # type: ignore
    from ._models import FileShareItem  # type: ignore
    from ._models import FileShareItems  # type: ignore
    from ._models import GeoReplicationStats  # type: ignore
    from ._models import IPRule  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import ImmutabilityPolicy  # type: ignore
    from ._models import ImmutabilityPolicyProperties  # type: ignore
    from ._models import ImmutableStorageAccount  # type: ignore
    from ._models import ImmutableStorageWithVersioning  # type: ignore
    from ._models import KeyCreationTime  # type: ignore
    from ._models import KeyPolicy  # type: ignore
    from ._models import KeyVaultProperties  # type: ignore
    from ._models import LastAccessTimeTrackingPolicy  # type: ignore
    from ._models import LeaseContainerRequest  # type: ignore
    from ._models import LeaseContainerResponse  # type: ignore
    from ._models import LeaseShareRequest  # type: ignore
    from ._models import LeaseShareResponse  # type: ignore
    from ._models import LegalHold  # type: ignore
    from ._models import LegalHoldProperties  # type: ignore
    from ._models import ListAccountSasResponse  # type: ignore
    from ._models import ListBlobInventoryPolicy  # type: ignore
    from ._models import ListContainerItem  # type: ignore
    from ._models import ListContainerItems  # type: ignore
    from ._models import ListQueue  # type: ignore
    from ._models import ListQueueResource  # type: ignore
    from ._models import ListQueueServices  # type: ignore
    from ._models import ListServiceSasResponse  # type: ignore
    from ._models import ListTableResource  # type: ignore
    from ._models import ListTableServices  # type: ignore
    from ._models import LocalUser  # type: ignore
    from ._models import LocalUserKeys  # type: ignore
    from ._models import LocalUserRegeneratePasswordResult  # type: ignore
    from ._models import LocalUsers  # type: ignore
    from ._models import ManagementPolicy  # type: ignore
    from ._models import ManagementPolicyAction  # type: ignore
    from ._models import ManagementPolicyBaseBlob  # type: ignore
    from ._models import ManagementPolicyDefinition  # type: ignore
    from ._models import ManagementPolicyFilter  # type: ignore
    from ._models import ManagementPolicyRule  # type: ignore
    from ._models import ManagementPolicySchema  # type: ignore
    from ._models import ManagementPolicySnapShot  # type: ignore
    from ._models import ManagementPolicyVersion  # type: ignore
    from ._models import MetricSpecification  # type: ignore
    from ._models import Multichannel  # type: ignore
    from ._models import NetworkRuleSet  # type: ignore
    from ._models import NetworkSecurityPerimeter  # type: ignore
    from ._models import NetworkSecurityPerimeterConfiguration  # type: ignore
    from ._models import NetworkSecurityPerimeterConfigurationList  # type: ignore
    from ._models import NetworkSecurityPerimeterConfigurationPropertiesProfile  # type: ignore
    from ._models import NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation  # type: ignore
    from ._models import NspAccessRule  # type: ignore
    from ._models import NspAccessRuleProperties  # type: ignore
    from ._models import NspAccessRulePropertiesSubscriptionsItem  # type: ignore
    from ._models import ObjectReplicationPolicies  # type: ignore
    from ._models import ObjectReplicationPolicy  # type: ignore
    from ._models import ObjectReplicationPolicyFilter  # type: ignore
    from ._models import ObjectReplicationPolicyRule  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PermissionScope  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import ProtectedAppendWritesHistory  # type: ignore
    from ._models import ProtocolSettings  # type: ignore
    from ._models import ProvisioningIssue  # type: ignore
    from ._models import ProvisioningIssueProperties  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import ProxyResourceAutoGenerated  # type: ignore
    from ._models import QueueServiceProperties  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceAccessRule  # type: ignore
    from ._models import ResourceAutoGenerated  # type: ignore
    from ._models import RestorePolicyProperties  # type: ignore
    from ._models import Restriction  # type: ignore
    from ._models import RoutingPreference  # type: ignore
    from ._models import SKUCapability  # type: ignore
    from ._models import SasPolicy  # type: ignore
    from ._models import ServiceSasParameters  # type: ignore
    from ._models import ServiceSpecification  # type: ignore
    from ._models import SignedIdentifier  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuInformation  # type: ignore
    from ._models import SmbSetting  # type: ignore
    from ._models import SshPublicKey  # type: ignore
    from ._models import StorageAccount  # type: ignore
    from ._models import StorageAccountCheckNameAvailabilityParameters  # type: ignore
    from ._models import StorageAccountCreateParameters  # type: ignore
    from ._models import StorageAccountInternetEndpoints  # type: ignore
    from ._models import StorageAccountKey  # type: ignore
    from ._models import StorageAccountListKeysResult  # type: ignore
    from ._models import StorageAccountListResult  # type: ignore
    from ._models import StorageAccountMicrosoftEndpoints  # type: ignore
    from ._models import StorageAccountMigration  # type: ignore
    from ._models import StorageAccountRegenerateKeyParameters  # type: ignore
    from ._models import StorageAccountSkuConversionStatus  # type: ignore
    from ._models import StorageAccountUpdateParameters  # type: ignore
    from ._models import StorageQueue  # type: ignore
    from ._models import StorageSkuListResult  # type: ignore
    from ._models import StorageTaskAssignment  # type: ignore
    from ._models import StorageTaskAssignmentExecutionContext  # type: ignore
    from ._models import StorageTaskAssignmentProperties  # type: ignore
    from ._models import StorageTaskAssignmentReport  # type: ignore
    from ._models import StorageTaskAssignmentUpdateExecutionContext  # type: ignore
    from ._models import StorageTaskAssignmentUpdateParameters  # type: ignore
    from ._models import StorageTaskAssignmentUpdateProperties  # type: ignore
    from ._models import StorageTaskAssignmentUpdateReport  # type: ignore
    from ._models import StorageTaskAssignmentsList  # type: ignore
    from ._models import StorageTaskReportInstance  # type: ignore
    from ._models import StorageTaskReportProperties  # type: ignore
    from ._models import StorageTaskReportSummary  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import Table  # type: ignore
    from ._models import TableAccessPolicy  # type: ignore
    from ._models import TableServiceProperties  # type: ignore
    from ._models import TableSignedIdentifier  # type: ignore
    from ._models import TagFilter  # type: ignore
    from ._models import TagProperty  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import TriggerParameters  # type: ignore
    from ._models import TriggerParametersUpdate  # type: ignore
    from ._models import UpdateHistoryProperty  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageListResult  # type: ignore
    from ._models import UsageName  # type: ignore
    from ._models import UserAssignedIdentity  # type: ignore
    from ._models import VirtualNetworkRule  # type: ignore

from ._storage_management_client_enums import (
    AccessTier,
    AccountImmutabilityPolicyState,
    AccountStatus,
    AccountType,
    AllowedCopyScope,
    AllowedMethods,
    BlobInventoryPolicyName,
    BlobRestoreProgressStatus,
    Bypass,
    CreatedByType,
    DefaultAction,
    DefaultSharePermission,
    DirectoryServiceOptions,
    DnsEndpointType,
    EnabledProtocols,
    EncryptionScopeSource,
    EncryptionScopeState,
    ExpirationAction,
    ExtendedLocationTypes,
    Format,
    GeoReplicationStatus,
    HttpProtocol,
    IdentityType,
    ImmutabilityPolicyState,
    ImmutabilityPolicyUpdateType,
    InventoryRuleType,
    IssueType,
    KeyPermission,
    KeySource,
    KeyType,
    Kind,
    LargeFileSharesState,
    LeaseContainerRequestEnum,
    LeaseDuration,
    LeaseShareAction,
    LeaseState,
    LeaseStatus,
    ListContainersInclude,
    ListEncryptionScopesInclude,
    ListLocalUserIncludeParam,
    ManagementPolicyName,
    MigrationName,
    MigrationState,
    MigrationStatus,
    MinimumTlsVersion,
    Name,
    NetworkSecurityPerimeterConfigurationProvisioningState,
    NspAccessRuleDirection,
    ObjectType,
    Permissions,
    PostFailoverRedundancy,
    PostPlannedFailoverRedundancy,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    PublicAccess,
    PublicNetworkAccess,
    Reason,
    ReasonCode,
    ResourceAssociationAccessMode,
    RootSquashType,
    RoutingChoice,
    RuleType,
    RunResult,
    RunStatusEnum,
    Schedule,
    Services,
    Severity,
    ShareAccessTier,
    SignedResource,
    SignedResourceTypes,
    SkuConversionStatus,
    SkuName,
    SkuTier,
    State,
    StorageAccountExpand,
    TriggerType,
    UsageUnit,
)

__all__ = [
    'AccessPolicy',
    'AccountImmutabilityPolicyProperties',
    'AccountSasParameters',
    'ActiveDirectoryProperties',
    'AzureEntityResource',
    'AzureFilesIdentityBasedAuthentication',
    'BlobContainer',
    'BlobInventoryCreationTime',
    'BlobInventoryPolicy',
    'BlobInventoryPolicyDefinition',
    'BlobInventoryPolicyFilter',
    'BlobInventoryPolicyRule',
    'BlobInventoryPolicySchema',
    'BlobRestoreParameters',
    'BlobRestoreRange',
    'BlobRestoreStatus',
    'BlobServiceItems',
    'BlobServiceProperties',
    'ChangeFeed',
    'CheckNameAvailabilityResult',
    'CloudErrorBody',
    'CorsRule',
    'CorsRules',
    'CustomDomain',
    'DateAfterCreation',
    'DateAfterModification',
    'DeleteRetentionPolicy',
    'DeletedAccount',
    'DeletedAccountListResult',
    'DeletedShare',
    'Dimension',
    'Encryption',
    'EncryptionIdentity',
    'EncryptionScope',
    'EncryptionScopeKeyVaultProperties',
    'EncryptionScopeListResult',
    'EncryptionService',
    'EncryptionServices',
    'Endpoints',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'ErrorResponseAutoGenerated',
    'ErrorResponseBody',
    'ExecutionTarget',
    'ExecutionTargetUpdate',
    'ExecutionTrigger',
    'ExecutionTriggerUpdate',
    'ExtendedLocation',
    'FileServiceItems',
    'FileServiceProperties',
    'FileShare',
    'FileShareItem',
    'FileShareItems',
    'GeoReplicationStats',
    'IPRule',
    'Identity',
    'ImmutabilityPolicy',
    'ImmutabilityPolicyProperties',
    'ImmutableStorageAccount',
    'ImmutableStorageWithVersioning',
    'KeyCreationTime',
    'KeyPolicy',
    'KeyVaultProperties',
    'LastAccessTimeTrackingPolicy',
    'LeaseContainerRequest',
    'LeaseContainerResponse',
    'LeaseShareRequest',
    'LeaseShareResponse',
    'LegalHold',
    'LegalHoldProperties',
    'ListAccountSasResponse',
    'ListBlobInventoryPolicy',
    'ListContainerItem',
    'ListContainerItems',
    'ListQueue',
    'ListQueueResource',
    'ListQueueServices',
    'ListServiceSasResponse',
    'ListTableResource',
    'ListTableServices',
    'LocalUser',
    'LocalUserKeys',
    'LocalUserRegeneratePasswordResult',
    'LocalUsers',
    'ManagementPolicy',
    'ManagementPolicyAction',
    'ManagementPolicyBaseBlob',
    'ManagementPolicyDefinition',
    'ManagementPolicyFilter',
    'ManagementPolicyRule',
    'ManagementPolicySchema',
    'ManagementPolicySnapShot',
    'ManagementPolicyVersion',
    'MetricSpecification',
    'Multichannel',
    'NetworkRuleSet',
    'NetworkSecurityPerimeter',
    'NetworkSecurityPerimeterConfiguration',
    'NetworkSecurityPerimeterConfigurationList',
    'NetworkSecurityPerimeterConfigurationPropertiesProfile',
    'NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation',
    'NspAccessRule',
    'NspAccessRuleProperties',
    'NspAccessRulePropertiesSubscriptionsItem',
    'ObjectReplicationPolicies',
    'ObjectReplicationPolicy',
    'ObjectReplicationPolicyFilter',
    'ObjectReplicationPolicyRule',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PermissionScope',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'ProtectedAppendWritesHistory',
    'ProtocolSettings',
    'ProvisioningIssue',
    'ProvisioningIssueProperties',
    'ProxyResource',
    'ProxyResourceAutoGenerated',
    'QueueServiceProperties',
    'Resource',
    'ResourceAccessRule',
    'ResourceAutoGenerated',
    'RestorePolicyProperties',
    'Restriction',
    'RoutingPreference',
    'SKUCapability',
    'SasPolicy',
    'ServiceSasParameters',
    'ServiceSpecification',
    'SignedIdentifier',
    'Sku',
    'SkuInformation',
    'SmbSetting',
    'SshPublicKey',
    'StorageAccount',
    'StorageAccountCheckNameAvailabilityParameters',
    'StorageAccountCreateParameters',
    'StorageAccountInternetEndpoints',
    'StorageAccountKey',
    'StorageAccountListKeysResult',
    'StorageAccountListResult',
    'StorageAccountMicrosoftEndpoints',
    'StorageAccountMigration',
    'StorageAccountRegenerateKeyParameters',
    'StorageAccountSkuConversionStatus',
    'StorageAccountUpdateParameters',
    'StorageQueue',
    'StorageSkuListResult',
    'StorageTaskAssignment',
    'StorageTaskAssignmentExecutionContext',
    'StorageTaskAssignmentProperties',
    'StorageTaskAssignmentReport',
    'StorageTaskAssignmentUpdateExecutionContext',
    'StorageTaskAssignmentUpdateParameters',
    'StorageTaskAssignmentUpdateProperties',
    'StorageTaskAssignmentUpdateReport',
    'StorageTaskAssignmentsList',
    'StorageTaskReportInstance',
    'StorageTaskReportProperties',
    'StorageTaskReportSummary',
    'SystemData',
    'Table',
    'TableAccessPolicy',
    'TableServiceProperties',
    'TableSignedIdentifier',
    'TagFilter',
    'TagProperty',
    'TrackedResource',
    'TriggerParameters',
    'TriggerParametersUpdate',
    'UpdateHistoryProperty',
    'Usage',
    'UsageListResult',
    'UsageName',
    'UserAssignedIdentity',
    'VirtualNetworkRule',
    'AccessTier',
    'AccountImmutabilityPolicyState',
    'AccountStatus',
    'AccountType',
    'AllowedCopyScope',
    'AllowedMethods',
    'BlobInventoryPolicyName',
    'BlobRestoreProgressStatus',
    'Bypass',
    'CreatedByType',
    'DefaultAction',
    'DefaultSharePermission',
    'DirectoryServiceOptions',
    'DnsEndpointType',
    'EnabledProtocols',
    'EncryptionScopeSource',
    'EncryptionScopeState',
    'ExpirationAction',
    'ExtendedLocationTypes',
    'Format',
    'GeoReplicationStatus',
    'HttpProtocol',
    'IdentityType',
    'ImmutabilityPolicyState',
    'ImmutabilityPolicyUpdateType',
    'InventoryRuleType',
    'IssueType',
    'KeyPermission',
    'KeySource',
    'KeyType',
    'Kind',
    'LargeFileSharesState',
    'LeaseContainerRequestEnum',
    'LeaseDuration',
    'LeaseShareAction',
    'LeaseState',
    'LeaseStatus',
    'ListContainersInclude',
    'ListEncryptionScopesInclude',
    'ListLocalUserIncludeParam',
    'ManagementPolicyName',
    'MigrationName',
    'MigrationState',
    'MigrationStatus',
    'MinimumTlsVersion',
    'Name',
    'NetworkSecurityPerimeterConfigurationProvisioningState',
    'NspAccessRuleDirection',
    'ObjectType',
    'Permissions',
    'PostFailoverRedundancy',
    'PostPlannedFailoverRedundancy',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ProvisioningState',
    'PublicAccess',
    'PublicNetworkAccess',
    'Reason',
    'ReasonCode',
    'ResourceAssociationAccessMode',
    'RootSquashType',
    'RoutingChoice',
    'RuleType',
    'RunResult',
    'RunStatusEnum',
    'Schedule',
    'Services',
    'Severity',
    'ShareAccessTier',
    'SignedResource',
    'SignedResourceTypes',
    'SkuConversionStatus',
    'SkuName',
    'SkuTier',
    'State',
    'StorageAccountExpand',
    'TriggerType',
    'UsageUnit',
]
