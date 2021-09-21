from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ProtocolControllerFilterSchema
from .schema import ProtocolControllerSchema
from .serializer import ProtocolSerializer
from .service import ProtocolService


@view_defaults(renderer='json')
class ProtocolController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ProtocolSerializer()
        self.service = ProtocolService()
        self.schema = ProtocolControllerSchema()
        self.filter_schema = ProtocolControllerFilterSchema()

    @view_config(route_name='get_all_protocols', permission='access.mks_crud_protocols')
    def get_all_protocols(self):
        filter_params = self.filter_schema.deserialize(self.request.GET)
        protocols = self.service.get_protocols(filter_params)
        return self.serializer.convert_list_to_json(protocols)

    @view_config(route_name='add_protocol', permission='access.mks_crud_protocols')
    def add_protocol(self):
        protocol_deserialized = self.schema.deserialize(self.request.json_body)
        protocol = self.serializer.convert_schema_to_object(protocol_deserialized)

        self.service.add_protocol(protocol)
        return {'id': protocol.protocol_id}

    @view_config(route_name='get_protocol', permission='access.mks_crud_protocols')
    def get_protocol(self):
        id = int(self.request.matchdict['id'])
        protocol = self.service.get_protocol_by_id(id)
        return self.serializer.convert_object_to_json(protocol)

    @view_config(route_name='delete_protocol', permission='access.mks_crud_protocols')
    def delete_protocol(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_protocol_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_protocol', permission='access.mks_crud_protocols')
    def edit_protocol(self):
        protocol_deserialized = self.schema.deserialize(self.request.json_body)
        protocol_deserialized['id'] = int(self.request.matchdict['id'])

        new_protocol = self.serializer.convert_schema_to_object(protocol_deserialized)
        self.service.update_protocol(new_protocol)
        return {'id': new_protocol.protocol_id}
