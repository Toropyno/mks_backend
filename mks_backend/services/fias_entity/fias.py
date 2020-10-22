from requests import Response

from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.fias import FIAS
from mks_backend.repositories.fias_entity.api import FIASAPIRepository
from mks_backend.services.fias_entity.utils import extract_addresses, get_addresses_with_AOID, \
    get_address_ending_with_socr_name, append_address


class FIASService:

    def __init__(self):
        self.search_address = ''
        self.repo = FIASAPIRepository()

    def append_address_if_in_row_address(self, row_address: str, socr_name: str, suitable_addresses: list) -> None:
        if socr_name + self.search_address.lower() in row_address.lower():
            address = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in address.lower():
                append_address(address, suitable_addresses)

    def get_addresses_from_response(self, search_text: str) -> list:
        fias_response = self.get_fias_response(search_text)
        return extract_addresses(fias_response)

    def get_AOID(self, search_address: str) -> str:
        return self.get_final_fias_address(search_address).get('AOID')

    def get_final_fias_address(self, search_address: str) -> dict:
        fias_response = self.get_final_fias_response(search_address)
        return get_addresses_with_AOID(fias_response)[0]

    def get_final_fias_response(self, search_text: str) -> Response:
        number_responses = self.repo.number_responses
        self.repo.number_responses = 1
        fias_response = self.get_fias_response(search_text)
        self.repo.number_responses = number_responses
        return fias_response

    def get_fias_response(self, search_text: str) -> Response:
        return self.repo.get_fias_response(search_text)

    @db_error_handler
    def add_fias(self, fias: FIAS) -> None:
        self.repo.add_fias(fias)
