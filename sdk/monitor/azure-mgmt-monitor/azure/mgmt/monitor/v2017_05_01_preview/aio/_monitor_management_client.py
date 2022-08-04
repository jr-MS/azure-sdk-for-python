# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models
from ._configuration import MonitorManagementClientConfiguration
from .operations import DiagnosticSettingsCategoryOperations, DiagnosticSettingsOperations, MetricDefinitionsOperations, MetricsOperations, SubscriptionDiagnosticSettingsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class MonitorManagementClient:
    """Monitor Management Client.

    :ivar diagnostic_settings_category: DiagnosticSettingsCategoryOperations operations
    :vartype diagnostic_settings_category:
     $(python-base-namespace).v2017_05_01_preview.aio.operations.DiagnosticSettingsCategoryOperations
    :ivar diagnostic_settings: DiagnosticSettingsOperations operations
    :vartype diagnostic_settings:
     $(python-base-namespace).v2017_05_01_preview.aio.operations.DiagnosticSettingsOperations
    :ivar metric_definitions: MetricDefinitionsOperations operations
    :vartype metric_definitions:
     $(python-base-namespace).v2017_05_01_preview.aio.operations.MetricDefinitionsOperations
    :ivar metrics: MetricsOperations operations
    :vartype metrics: $(python-base-namespace).v2017_05_01_preview.aio.operations.MetricsOperations
    :ivar subscription_diagnostic_settings: SubscriptionDiagnosticSettingsOperations operations
    :vartype subscription_diagnostic_settings:
     $(python-base-namespace).v2017_05_01_preview.aio.operations.SubscriptionDiagnosticSettingsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2017-05-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = MonitorManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.diagnostic_settings_category = DiagnosticSettingsCategoryOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.diagnostic_settings = DiagnosticSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.metric_definitions = MetricDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.metrics = MetricsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.subscription_diagnostic_settings = SubscriptionDiagnosticSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MonitorManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
