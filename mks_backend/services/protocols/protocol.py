from typing import List

from mks_backend.models.protocols.protocol import Protocol
from mks_backend.repositories.protocol import ProtocolRepository
from mks_backend.services.filestorage import FilestorageService


class ProtocolService:

    def __init__(self):
        self.repo = ProtocolRepository()
        self.filestorage_service = FilestorageService()

    def get_protocols(self, filter_params=None) -> List[Protocol]:
        if not filter_params:
            protocols = self.repo.get_all_protocols()
        else:
            filter_params = self.switch_case(filter_params)
            protocols = self.filter_protocols(filter_params)

        return protocols

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
        self.filestorage_service.compare_two_filestorages(new_idfilestorage, old_idfilestorage)

    def delete_protocol_by_id_with_filestorage_cascade(self, id: int) -> None:
        protocol = self.repo.get_protocol_by_id(id)
        self.repo.delete_protocol(protocol)
        self.filestorage_service.delete_filestorage_by_id(protocol.idfilestorage)

    def switch_case(self, filter_params: dict) -> dict:
        case_switcher = {
            'dateStart': 'date_start',
            'dateEnd': 'date_end',
            'protocolNumber': 'protocol_number',
            'meeting': 'meeting',
            'protocolName': 'protocol_name',
        }

        params = dict()
        for key, value in filter_params.items():
            if key in case_switcher and value is not None:
                params[case_switcher[key]] = filter_params[key]

        return params

    def filter_protocols(self, params: dict) -> list:
        return self.repo.filter_protocols(params)
