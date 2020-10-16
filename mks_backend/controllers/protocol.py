from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.controllers.schemas.protocol import ProtocolControllerFilterSchema
from mks_backend.controllers.schemas.protocol import ProtocolControllerSchema
from mks_backend.serializers.protocol import ProtocolSerializer
from mks_backend.services.protocol import ProtocolService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error


class ProtocolController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ProtocolSerializer()
        self.service = ProtocolService()
        self.schema = ProtocolControllerSchema()

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='get_all_protocols', renderer='json')
    def get_all_protocols(self):
        if self.request.params:
            params_schema = ProtocolControllerFilterSchema()
            params_deserialized = params_schema.deserialize(self.request.GET)
            params = self.service.get_params_from_schema(params_deserialized)
            protocols = self.service.filter_protocols(params)
        else:
            protocols = self.service.get_all_protocols()

        return self.serializer.convert_list_to_json(protocols)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_protocol', renderer='json')
    def add_protocol(self):
        protocol_deserialized = self.schema.deserialize(self.request.json_body)
        protocol = self.serializer.convert_schema_to_object(protocol_deserialized)

        self.service.add_protocol(protocol)
        return {'id': protocol.protocol_id}

    @view_config(route_name='get_protocol', renderer='json')
    def get_protocol(self):
        id = int(self.request.matchdict['id'])
        protocol = self.service.get_protocol_by_id(id)
        return self.serializer.convert_object_to_json(protocol)

    @view_config(route_name='delete_protocol', renderer='json')
    def delete_protocol(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_protocol_by_id_with_filestorage_cascade(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_protocol', renderer='json')
    def edit_protocol(self):
        protocol_deserialized = self.schema.deserialize(self.request.json_body)
        protocol_deserialized['id'] = int(self.request.matchdict['id'])

        new_protocol = self.serializer.convert_schema_to_object(protocol_deserialized)
        self.service.update_protocol(new_protocol)
        return {'id': new_protocol.protocol_id}
