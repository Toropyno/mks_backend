from mks_backend.repositories.protocols_repository import ProtocolRepository
from mks_backend.services.filestorage_service import FilestorageService
from mks_backend.models.protocol import Protocol


class ProtocolService(object):
    def __init__(self):
        self.repo = ProtocolRepository()

    def get_all_protocols(self):
        return self.repo.get_all_protocols().all()

    def get_protocol_by_id(self, id):
        return self.repo.get_protocol_by_id(id)

    def get_protocol_from_request(self, request_data):
        protocol_num = request_data.get('protocolNumber')
        protocol_date = request_data.get('protocolDate')
        meetings_type_id = request_data.get('meetingsTypeId')
        protocol_name = request_data.get('protocolName')
        note = request_data.get('note')
        idfilestorage = request_data.get('idFileStorage')

        return Protocol(protocol_num=protocol_num,
                        protocol_date=protocol_date,
                        meetings_type_id=meetings_type_id,
                        protocol_name=protocol_name,
                        note=note,
                        idfilestorage=idfilestorage)

    def add_protocol(self, protocol):
        return self.repo.add_protocol(protocol)

    def update_protocol(self, id, new_protocol):
        old_protocol = self.repo.get_protocol_by_id(id)
        new_protocol.protocol_id = old_protocol.protocol_id

        old_idfilestorage = old_protocol.idfilestorage
        new_idfilestorage = new_protocol.idfilestorage

        self.repo.update_protocol(new_protocol)
        FilestorageService.compare_two_filestorages(new_idfilestorage, old_idfilestorage)
        return new_protocol

    def delete_protocol_by_id(self, id):
        return self.repo.delete_protocol_by_id(id)
