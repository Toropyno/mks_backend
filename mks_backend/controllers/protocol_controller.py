import re
from datetime import datetime

import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.serializers.protocol_serializer import ProtocolSerializer
from mks_backend.services.protocol_service import ProtocolService


class ProtocolController(object):

    def __init__(self, request):
        self.request = request
        self.serializer = ProtocolSerializer()
        self.service = ProtocolService()

    @view_config(route_name='protocols', request_method='GET', renderer='json')
    def get_all_protocols(self):
        if self.request.params:
            from mks_backend.controllers.schemas.protocol_schema import ProtocolControllerFilterSchema
            params_schema = ProtocolControllerFilterSchema()
            try:
                params_deserialized = params_schema.deserialize(self.request.GET)
            except colander.Invalid as error:
                return Response(status=403, json_body=error.asdict())
            except ValueError as date_parse_error:
                return Response(status=403, json_body=date_parse_error.args)
            params = self.service.get_params_from_schema(params_deserialized)
            protocols_array = self.service.filter_protocols(params)
        else:
            protocols_array = self.service.get_all_protocols()

        json = self.serializer.convert_list_to_json(protocols_array)
        return json

    @view_config(route_name='add_protocol', request_method='POST', renderer='json')
    def add_protocol(self):
        from mks_backend.controllers.schemas.protocol_schema import ProtocolControllerSchema
        protocol_schema = ProtocolControllerSchema()
        try:
            protocol_deserialized = protocol_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        protocol = self.serializer.convert_schema_to_object(protocol_deserialized)
        self.service.add_protocol(protocol)
        return {'id': protocol.protocol_id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='GET', renderer='json')
    def get_protocol(self):
        id = self.request.matchdict['id']
        protocol = self.service.get_protocol_by_id(id)
        json = self.serializer.convert_object_to_json(protocol)
        return json

    @view_config(route_name='protocols_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_protocol(self):
        id = self.request.matchdict['id']
        self.service.delete_protocol_by_id_with_filestorage_cascade(id)
        return {'id': id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_protocol(self):
        from mks_backend.controllers.schemas.protocol_schema import ProtocolControllerSchema
        protocol_schema = ProtocolControllerSchema()
        id = self.request.matchdict['id']
        try:
            protocol_deserialized = protocol_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        protocol_deserialized["id"] = id
        new_protocol = self.serializer.convert_schema_to_object(protocol_deserialized)
        new_protocol = self.service.update_protocol(new_protocol)
        return {'id': new_protocol.protocol_id}


