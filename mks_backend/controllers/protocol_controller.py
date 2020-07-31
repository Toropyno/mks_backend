from pyramid.view import view_config, view_defaults

from mks_backend.repositories.protocols_repository import ProtocolRepository
from mks_backend.serializers.protocol_serializer import ProtocolSerializer
from mks_backend.services.protocol_service import ProtocolService
from mks_backend.models.protocol import Protocol


class ProtocolController(object):
    def __init__(self, request):
        self.request = request
        self.repository = ProtocolRepository()
        self.serializer = ProtocolSerializer()
        self.service = ProtocolService()

    @view_config(route_name='protocols_delete_change_and_view', request_method='GET', renderer='json')
    def get_protocol(self):
        id = self.request.matchdict['id']
        protocol = self.repository.get_protocol_by_id(id)
        json = self.serializer.convert_object_to_json(protocol)
        return json

    @view_config(route_name='protocols', request_method='GET', renderer='json')
    def get_all_protocols(self):
        protocols_array = self.repository.get_all_protocols()
        json = self.serializer.convert_list_to_json(protocols_array)
        return json

    @view_config(route_name='add_protocol', request_method='POST', renderer='json')
    def add_protocol(self):
        protocol = self.get_protocol_object_from_request_params()
        self.repository.add_protocol(protocol)
        return {'id': protocol.protocol_id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_protocol(self):
        id = self.request.matchdict['id']
        self.repository.delete_protocol_by_id(id)
        return {'id': id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_protocol(self):
        protocol_id = self.request.matchdict['id']
        protocol = self.get_protocol_object_from_request_params()
        protocol.protocol_id = protocol_id
        self.repository.update_protocol(protocol)
        return {'id': protocol_id}

    def get_protocol_object_from_request_params(self):
        protocol_num = self.request.json_body.get('protocolNumber')
        protocol_date = self.request.json_body.get('protocolDate')
        meetings_type_id = self.request.json_body.get('meetingsTypeId')
        protocol_name = self.request.json_body.get('protocolName')
        note = self.request.json_body.get('note')
        idfilestorage = self.request.json_body.get('idFileStorage')

        return Protocol(protocol_num=protocol_num,
                        protocol_date=protocol_date,
                        meetings_type_id=meetings_type_id,
                        protocol_name=protocol_name,
                        note=note,
                        idfilestorage=idfilestorage)
