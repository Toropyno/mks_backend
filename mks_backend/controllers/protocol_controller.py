from pyramid.view import view_config

from mks_backend.repositories.protocols_repository import ProtocolRepository
from mks_backend.serializers.protocol_serializer import ProtocolSerializer
from mks_backend.services.protocol_service import ProtocolService

from pyramid.response import Response

import colander


class ProtocolController(object):
    def __init__(self, request):
        self.request = request
        self.repository = ProtocolRepository()
        self.serializer = ProtocolSerializer()
        self.service = ProtocolService()

    @view_config(route_name='protocols', request_method='GET', renderer='json')
    def get_all_protocols(self):
        if self.request.params:
            params_schema = ProtocolControllerFilterSchema()
            try:
                params_deserialized = params_schema.deserialize(self.request.GET)
                params = self.service.get_params_from_schema(params_deserialized)
            except colander.Invalid as error:
                return Response(status=403, json_body=error.asdict())
            except ValueError as date_parse_error:
                return Response(status=403, json_body=date_parse_error.args)

            protocols_array = self.repository.get_all_protocols()
            protocols_array = self.repository.filter_protocols(protocols_array, params)
            json = self.serializer.convert_list_to_json(protocols_array)
            return json
        else:
            protocols_array = self.service.get_all_protocols()
            json = self.serializer.convert_list_to_json(protocols_array)
            return json

    @view_config(route_name='add_protocol', request_method='POST', renderer='json')
    def add_protocol(self):
        protocol_schema = ProtocolControllerSchema()
        try:
            protocol_deserialized = protocol_schema.deserialize(self.request.GET)
            protocol = self.serializer.convert_schema_to_object(protocol_deserialized)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)

        self.repository.add_protocol(protocol)
        return {'id': protocol.protocol_id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='GET', renderer='json')
    def get_protocol(self):
        protocol_schema = ProtocolControllerIdSchema()
        try:
            protocol_deserialized = protocol_schema.deserialize(self.request.GET)
            id = protocol_deserialized['id']
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        protocol = self.repository.get_protocol_by_id(id)
        json = self.serializer.convert_object_to_json(protocol)
        return json

    @view_config(route_name='protocols_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_protocol(self):
        protocol_schema = ProtocolControllerIdSchema()
        try:
            protocol_deserialized = protocol_schema.deserialize(self.request.GET)
            id = protocol_deserialized['id']
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        self.service.delete_protocol_by_id(id)
        return {'id': id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_protocol(self):
        protocol_schema = ProtocolControllerSchema()
        protocol_id_schema = ProtocolControllerIdSchema()
        try:
            protocol_id_deserialized = protocol_id_schema.deserialize(self.request.GET)
            id = protocol_id_deserialized['id']
            protocol_deserialized = protocol_schema.deserialize(self.request.GET)
            protocol_deserialized["id"] = id
            new_protocol = self.serializer.convert_schema_to_object(protocol_deserialized)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)

        new_protocol = self.service.update_protocol(new_protocol.protocol_id, new_protocol)
        return {'id': new_protocol.protocol_id}


class ProtocolControllerIdSchema(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int(), name='id', validator=colander.Range(min=0))

class ProtocolControllerSchema(colander.MappingSchema):
    protocol_num = colander.SchemaNode(colander.String(), name='protocolNumber')
    protocol_date = colander.SchemaNode(colander.Date('%d.%m.%Y'), name='protocolDate')
    meetings_type_id = colander.SchemaNode(colander.Int(), name='meeting', validator=colander.Range(min=0))
    protocol_name = colander.SchemaNode(colander.String(), name='protocolName')
    note = colander.SchemaNode(colander.String(), name='note')
    #idfilestorage = colander.SchemaNode(colander.String(), name='idFileStorage')

class ProtocolControllerFilterSchema(colander.MappingSchema):
    protocol_num = colander.SchemaNode(colander.String(), name='protocolNumber', default=colander.drop)
    meetings_type_id = colander.SchemaNode(colander.Int(), name='meeting', validator=colander.Range(min=0), default=colander.drop)
    protocol_name = colander.SchemaNode(colander.String(), name='protocolName', default=colander.drop)
    date_start = colander.SchemaNode(colander.Date('%d.%m.%Y'), name='dateStart', default=colander.drop)
    date_end = colander.SchemaNode(colander.Date('%d.%m.%Y'), name='dateEnd', default=colander.drop)
