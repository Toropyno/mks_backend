from mks_backend.services.fias_entity import SUBJECT_SOCR_NAMES
from mks_backend.services.fias_entity.address import FIASAPIService

from mks_backend.services.fias_entity.utils import get_by_socr_name, append_address

from mks_backend.errors.fias_error import FIASError, fias_error_handler


class SubjectService:

    def __init__(self):
        self.search_subject = ''
        self.subjects = set()
        self.service_api = FIASAPIService()

    @fias_error_handler
    def get_subjects_hints(self) -> set:
        self.subjects = set()

        addresses = self.get_addresses_from_fias_api()
        if not addresses:
            raise FIASError('cannotFindAddress')

        for row_address in addresses:
            for socr in SUBJECT_SOCR_NAMES:
                self.append_subject_if_in_row_address(row_address, socr)

        return self.subjects

    def get_addresses_from_fias_api(self) -> list:
        return self.service_api.get_addresses_from_response(self.search_subject)

    def append_subject_if_in_row_address(self, row_address: str, socr_name: str) -> None:
        if socr_name.lower() + self.search_subject.lower() in row_address.lower():
            subject = get_by_socr_name(row_address, socr_name)

            if socr_name.lower() + self.search_subject.lower() in subject.lower():
                append_address(subject, self.subjects)
