from mks_backend.repositories.protocols_repository import ProtocolRepository
from mks_backend.services.filestorage_service import FilestorageService
from mks_backend.models.protocol import Protocol
from mks_backend.repositories.filestorage_hdd import FilestorageHDD


class ProtocolService(object):
    def __init__(self):
        self.repo = ProtocolRepository()

    def get_all_protocols(self):
        return self.repo.get_all_protocols().all()

    def get_protocol_by_id(self, id):
        return self.repo.get_protocol_by_id(id)

    def add_protocol(self, protocol):
        return self.repo.add_protocol(protocol)

    def update_protocol(self, new_protocol):
        old_protocol = self.repo.get_protocol_by_id(new_protocol.protocol_id)
        new_protocol.protocol_id = old_protocol.protocol_id

        old_idfilestorage = old_protocol.idfilestorage
        new_idfilestorage = new_protocol.idfilestorage

        self.repo.update_protocol(new_protocol)
        FilestorageService.compare_two_filestorages(new_idfilestorage, old_idfilestorage)
        return new_protocol

    def delete_protocol_by_id(self, id):
        filestorage_id = self.repo.get_protocol_by_id(id).idfilestorage
        FilestorageHDD.delete_by_id(filestorage_id)

        self.repo.delete_protocol_by_id(id)

    def get_params_from_schema(self, schema_dict):
        params = {}
        if 'dateStart' in schema_dict:
            params['dateStart'] = schema_dict['dateStart']
        if 'dateEnd' in schema_dict:
            params['dateEnd'] = schema_dict['dateEnd']
        if 'protocolNumber' in schema_dict:
            params['protocolNumber'] = schema_dict['protocolNumber']
        if 'meeting' in schema_dict:
            params['meeting'] = schema_dict['meeting']
        if 'protocolName' in schema_dict:
            params['protocolName'] = schema_dict['protocolName']
        return params

