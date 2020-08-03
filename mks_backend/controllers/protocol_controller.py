from pyramid.view import view_config

from mks_backend.repositories.protocols_repository import ProtocolRepository
from mks_backend.serializers.protocol_serializer import ProtocolSerializer
from mks_backend.services.protocol_service import ProtocolService


class ProtocolController(object):
    def __init__(self, request):
        self.request = request
        self.repository = ProtocolRepository()
        self.serializer = ProtocolSerializer()
        self.service = ProtocolService()

    @view_config(route_name='protocols', request_method='GET', renderer='json')
    def get_all_protocols(self):
        if self.request.params:
            params = dict(self.request.params)
            filter_dict = dict(zip(params.keys(), params.values()))
            protocols_array = self.repository.get_all_protocols()
            protocols_array = self.repository.filter_protocols(protocols_array, filter_dict)
            json = self.serializer.convert_list_to_json(protocols_array)
            return json
        else:
            protocols_array = self.service.get_all_protocols()
            json = self.serializer.convert_list_to_json(protocols_array)
            return json

    @view_config(route_name='add_protocol', request_method='POST', renderer='json')
    def add_protocol(self):
        protocol = self.service.get_protocol_from_request(self.request.json_body)
        self.repository.add_protocol(protocol)
        return {'id': protocol.protocol_id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='GET', renderer='json')
    def get_protocol(self):
        id = self.request.matchdict['id']
        protocol = self.repository.get_protocol_by_id(id)
        json = self.serializer.convert_object_to_json(protocol)
        return json

    @view_config(route_name='protocols_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_protocol(self):
        id = self.request.matchdict['id']
        self.service.delete_protocol_by_id(id)
        return {'id': id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_protocol(self):
        new_protocol = self.service.get_protocol_from_request(self.request.json_body)
        new_protocol = self.service.update_protocol(self.request.matchdict['id'], new_protocol)
        return {'id': new_protocol.protocol_id}
