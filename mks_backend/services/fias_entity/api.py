from requests import Response

from mks_backend.services.fias_entity.utils import (
    extract_addresses,
    get_address_ending_with_socr_name,
    append_address,
    get_search_address
)

from mks_backend.services.fias_entity import (
    SUBJECT_SORC_NAMES,
    CITY_SORC_NAMES,
    LOCALITY_SORC_NAMES,
    REMAINING_SORC_NAMES,
    DISTRICT_SORC_NAMES
)

from mks_backend.models.fias import FIAS
from mks_backend.repositories.fias_entity.api import FIASAPIRepository


class FIASAPIService:

    def __init__(self):
        self.search_address = ''
        self.repo = FIASAPIRepository()

    def create_full_fias_hints(self, full_fias):
        number_responses = self.repo.number_responses
        self.repo.number_responses = 5

        fias_response = self.get_addresses_from_response(full_fias)

        self.repo.number_responses = number_responses
        return fias_response

    def append_address_if_in_row_address(self, row_address: str, socr_name: str, suitable_addresses: list) -> None:
        if socr_name + self.search_address.lower() in row_address.lower():
            address = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in address.lower():
                append_address(address, suitable_addresses)

    def get_addresses_from_response(self, search_address: str) -> list:
        fias_response = self.get_fias_response(search_address)
        return extract_addresses(fias_response)

    def get_final_address(self, fias: FIAS) -> dict:
        search_address = get_search_address(fias)
        fias_response = self.get_final_fias_address(search_address)[0]
        if not fias_response:
            return {}
        return fias_response.get('text') + '. ' + fias_response.get('aoid')

    def get_final_fias_address(self, search_address: str) -> dict:
        number_responses = self.repo.number_responses
        self.repo.number_responses = 1

        fias_response = self.get_fias_response(search_address)

        if search_address[-7:] != fias_response.json()[0].get('text')[-7:]:
            return {}
      
        self.repo.number_responses = number_responses
        return fias_response.json()

    def get_fias_response(self, search_address: str) -> Response:
        return self.repo.get_fias_response(search_address)

    def split_full_fias(self, full_fias: str):
        street = 0
        for name in REMAINING_SORC_NAMES:
            if name in full_fias:
                street += 1
        if street == 0:
            return

        fias = FIAS()

        aoid = self.get_aoid(full_fias)
        if not aoid:
            return None
        fias.aoid = aoid

        address_by_aoid = self.repo.get_by_aoid_response(aoid).json()
        fill_in_all_fields(address_by_aoid, fias)
        if not fias.remaining_address:
            return None
        return fias

    def get_aoid(self, search_address: str) -> str:
        final_address = self.get_final_fias_address(search_address)
        if not final_address:
            return ''
        final_address = final_address[0]
        return final_address.get('aoid')


def fill_in_all_fields(address_by_aoid, fias) -> None:
    subject = ''
    district = ''
    city = ''
    locality = ''
    remaining_address = ''

    for row in address_by_aoid:
        subject_row = fill_in_field(row, SUBJECT_SORC_NAMES)
        if subject_row:
            subject += subject_row + ' '

        district_row = fill_in_field(row, DISTRICT_SORC_NAMES)
        if district_row:
            district += district_row + ' '

        city_row = fill_in_field(row, CITY_SORC_NAMES)
        if city_row:
            city += city_row + ' '

        locality_row = fill_in_field(row, LOCALITY_SORC_NAMES)
        if locality_row:
            locality += locality_row + ' '

        remaining_address_row = fill_in_field(row, REMAINING_SORC_NAMES)
        if remaining_address_row:
            remaining_address += remaining_address_row + ' '

    if subject:
        fias.subject = subject.strip(' ')
    if district:
        fias.district = district.strip(' ')
    if city:
        fias.city = city.strip(' ')
    if locality:
        fias.locality = locality.strip(' ')
    if remaining_address:
        fias.remaining_address = remaining_address.strip(' ')


def fill_in_field(row: dict, socr_names: list) -> str:
    for socr_name in socr_names:
        if socr_name.strip(' ') == row.get('shortname'):
            return row.get('shortname') + ' ' + row.get('formalname')
