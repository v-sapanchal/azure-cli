# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network virtual-appliance connection update",
)
class Update(AAZCommand):
    """Update existing connection to Network Virtual Appliance

    :example: Update NVA connection routing configuration - change associated route table
        az network virtual-appliance connection update --name defaultConnection  --nva MyNva -g MyRG --subscription <subId> --associated-route-table "{'id': '/subscriptions/<subId>/resourceGroups/<MyRG>/providers/Microsoft.Network/virtualHubs/<vhubName>/hubRouteTables/<customRouteTable>'}"

    :example: Update NVA connection routing configuration - add Propagated route table Labels
        az network virtual-appliance connection update --name defaultConnection  --nva MyNva -g MyRG --subscription <subId>  --labels [label1,label2]

    :example: Update NVA connection routing configuration - add propagated route table id
        az network virtual-appliance connection update --name defaultConnection  --nva MyNva -g MyRG --subscription <subId>   --propagated "[{'id':'<routeTable1id>'},{'id':'<routeTable2id>'}]"
    """

    _aaz_info = {
        "version": "2023-06-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkvirtualappliances/{}/networkvirtualapplianceconnections/{}", "2023-06-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the NVA connection.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.virtual_appliance_name = AAZStrArg(
            options=["--nva", "--virtual-appliance-name"],
            help="The name of the Network Virtual Appliance.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "NetworkVirtualApplianceConnectionParameters"

        # define Arg Group "PropagatedRouteTables"

        _args_schema = cls._args_schema
        _args_schema.propagated_route_table_ids = AAZListArg(
            options=["--propagated", "--propagated-route-table-ids"],
            arg_group="PropagatedRouteTables",
            help="List of resource id of propagated route tables.",
            nullable=True,
        )
        _args_schema.propagated_route_table_labels = AAZListArg(
            options=["--labels", "--propagated-route-table-labels"],
            arg_group="PropagatedRouteTables",
            help="The list of labels.",
            nullable=True,
        )

        propagated_route_table_ids = cls._args_schema.propagated_route_table_ids
        propagated_route_table_ids.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_sub_resource_update(propagated_route_table_ids.Element)

        propagated_route_table_labels = cls._args_schema.propagated_route_table_labels
        propagated_route_table_labels.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        # define Arg Group "RoutingConfiguration"

        _args_schema = cls._args_schema
        _args_schema.associated_route_table = AAZObjectArg(
            options=["--associated-route-table"],
            arg_group="RoutingConfiguration",
            help="The resource id RouteTable associated with this RoutingConfiguration.",
            nullable=True,
        )
        cls._build_args_sub_resource_update(_args_schema.associated_route_table)
        _args_schema.inbound_route_map = AAZObjectArg(
            options=["--inbound-route-map"],
            arg_group="RoutingConfiguration",
            help="The resource id of the RouteMap associated with this RoutingConfiguration for inbound learned routes.",
            nullable=True,
        )
        cls._build_args_sub_resource_update(_args_schema.inbound_route_map)
        _args_schema.outbound_route_map = AAZObjectArg(
            options=["--outbound-route-map"],
            arg_group="RoutingConfiguration",
            help="The resource id of theRouteMap associated with this RoutingConfiguration for outbound advertised routes.",
            nullable=True,
        )
        cls._build_args_sub_resource_update(_args_schema.outbound_route_map)
        return cls._args_schema

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.NetworkVirtualApplianceConnectionsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.NetworkVirtualApplianceConnectionsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetworkVirtualApplianceConnectionsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkVirtualApplianceName", self.ctx.args.virtual_appliance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-06-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_network_virtual_appliance_connection_read(cls._schema_on_200)

            return cls._schema_on_200

    class NetworkVirtualApplianceConnectionsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/networkVirtualApplianceConnections/{connectionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkVirtualApplianceName", self.ctx.args.virtual_appliance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-06-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_network_virtual_appliance_connection_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("name", AAZStrType, ".name")
                properties.set_prop("routingConfiguration", AAZObjectType)

            routing_configuration = _builder.get(".properties.routingConfiguration")
            if routing_configuration is not None:
                _UpdateHelper._build_schema_sub_resource_update(routing_configuration.set_prop("associatedRouteTable", AAZObjectType, ".associated_route_table"))
                _UpdateHelper._build_schema_sub_resource_update(routing_configuration.set_prop("inboundRouteMap", AAZObjectType, ".inbound_route_map"))
                _UpdateHelper._build_schema_sub_resource_update(routing_configuration.set_prop("outboundRouteMap", AAZObjectType, ".outbound_route_map"))
                routing_configuration.set_prop("propagatedRouteTables", AAZObjectType)

            propagated_route_tables = _builder.get(".properties.routingConfiguration.propagatedRouteTables")
            if propagated_route_tables is not None:
                propagated_route_tables.set_prop("ids", AAZListType, ".propagated_route_table_ids")
                propagated_route_tables.set_prop("labels", AAZListType, ".propagated_route_table_labels")

            ids = _builder.get(".properties.routingConfiguration.propagatedRouteTables.ids")
            if ids is not None:
                _UpdateHelper._build_schema_sub_resource_update(ids.set_elements(AAZObjectType, "."))

            labels = _builder.get(".properties.routingConfiguration.propagatedRouteTables.labels")
            if labels is not None:
                labels.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_network_virtual_appliance_connection_read = None

    @classmethod
    def _build_schema_network_virtual_appliance_connection_read(cls, _schema):
        if cls._schema_network_virtual_appliance_connection_read is not None:
            _schema.id = cls._schema_network_virtual_appliance_connection_read.id
            _schema.properties = cls._schema_network_virtual_appliance_connection_read.properties
            return

        cls._schema_network_virtual_appliance_connection_read = _schema_network_virtual_appliance_connection_read = AAZObjectType()

        network_virtual_appliance_connection_read = _schema_network_virtual_appliance_connection_read
        network_virtual_appliance_connection_read.id = AAZStrType()
        network_virtual_appliance_connection_read.properties = AAZObjectType()

        properties = _schema_network_virtual_appliance_connection_read.properties
        properties.asn = AAZIntType()
        properties.bgp_peer_address = AAZListType(
            serialized_name="bgpPeerAddress",
        )
        properties.enable_internet_security = AAZBoolType(
            serialized_name="enableInternetSecurity",
        )
        properties.name = AAZStrType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.routing_configuration = AAZObjectType(
            serialized_name="routingConfiguration",
        )
        properties.tunnel_identifier = AAZIntType(
            serialized_name="tunnelIdentifier",
        )

        bgp_peer_address = _schema_network_virtual_appliance_connection_read.properties.bgp_peer_address
        bgp_peer_address.Element = AAZStrType()

        routing_configuration = _schema_network_virtual_appliance_connection_read.properties.routing_configuration
        routing_configuration.associated_route_table = AAZObjectType(
            serialized_name="associatedRouteTable",
        )
        cls._build_schema_sub_resource_read(routing_configuration.associated_route_table)
        routing_configuration.inbound_route_map = AAZObjectType(
            serialized_name="inboundRouteMap",
        )
        cls._build_schema_sub_resource_read(routing_configuration.inbound_route_map)
        routing_configuration.outbound_route_map = AAZObjectType(
            serialized_name="outboundRouteMap",
        )
        cls._build_schema_sub_resource_read(routing_configuration.outbound_route_map)
        routing_configuration.propagated_route_tables = AAZObjectType(
            serialized_name="propagatedRouteTables",
        )
        routing_configuration.vnet_routes = AAZObjectType(
            serialized_name="vnetRoutes",
        )

        propagated_route_tables = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.propagated_route_tables
        propagated_route_tables.ids = AAZListType()
        propagated_route_tables.labels = AAZListType()

        ids = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.propagated_route_tables.ids
        ids.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(ids.Element)

        labels = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.propagated_route_tables.labels
        labels.Element = AAZStrType()

        vnet_routes = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.vnet_routes
        vnet_routes.bgp_connections = AAZListType(
            serialized_name="bgpConnections",
            flags={"read_only": True},
        )
        vnet_routes.static_routes = AAZListType(
            serialized_name="staticRoutes",
        )
        vnet_routes.static_routes_config = AAZObjectType(
            serialized_name="staticRoutesConfig",
        )

        bgp_connections = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.vnet_routes.bgp_connections
        bgp_connections.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(bgp_connections.Element)

        static_routes = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.vnet_routes.static_routes
        static_routes.Element = AAZObjectType()

        _element = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.vnet_routes.static_routes.Element
        _element.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )
        _element.name = AAZStrType()
        _element.next_hop_ip_address = AAZStrType(
            serialized_name="nextHopIpAddress",
        )

        address_prefixes = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.vnet_routes.static_routes.Element.address_prefixes
        address_prefixes.Element = AAZStrType()

        static_routes_config = _schema_network_virtual_appliance_connection_read.properties.routing_configuration.vnet_routes.static_routes_config
        static_routes_config.propagate_static_routes = AAZBoolType(
            serialized_name="propagateStaticRoutes",
            flags={"read_only": True},
        )
        static_routes_config.vnet_local_route_override_criteria = AAZStrType(
            serialized_name="vnetLocalRouteOverrideCriteria",
        )

        _schema.id = cls._schema_network_virtual_appliance_connection_read.id
        _schema.properties = cls._schema_network_virtual_appliance_connection_read.properties

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Update"]