from mks_backend.models.protocols.protocol import Protocol
from mks_backend.repositories.filestorage import FilestorageRepository
from mks_backend.repositories.filestorage_hdd import FilestorageHDD
from mks_backend.repositories.protocol import ProtocolRepository
from mks_backend.services.filestorage import FilestorageService


class ProtocolService:

    def __init__(self):
        self.repo = ProtocolRepository()

    def get_all_protocols(self) -> list:
        return self.repo.get_all_protocols()

    def get_protocol_by_id(self, id) -> Protocol:
        return self.repo.get_protocol_by_id(id)

    def add_protocol(self, protocol: Protocol) -> None:
        self.repo.add_protocol(protocol)

    def update_protocol(self, new_protocol: Protocol) -> None:
        old_protocol = self.repo.get_protocol_by_id(new_protocol.protocol_id)
        new_protocol.protocol_id = old_protocol.protocol_id

        old_idfilestorage = old_protocol.idfilestorage
        new_idfilestorage = new_protocol.idfilestorage

        self.repo.update_protocol(new_protocol)
        FilestorageService.compare_two_filestorages(new_idfilestorage, old_idfilestorage)

    def delete_protocol_by_id_with_filestorage_cascade(self, id: int) -> None:
        protocol = self.repo.get_protocol_by_id(id)
        FilestorageHDD.delete_by_id(protocol.idfilestorage)

        self.repo.delete_protocol(protocol)
        FilestorageRepository.delete_filestorage_by_id(protocol.idfilestorage)

    def get_params_from_schema(self, schema_dict: dict) -> dict:
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

    def filter_protocols(self, params: dict) -> list:
        return self.repo.filter_protocols(params)
