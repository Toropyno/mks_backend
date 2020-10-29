from requests import Response

from mks_backend.services.fias_entity.utils import (
    extract_addresses,
    get_address_ending_with_socr_name,
    append_address,
    get_search_address,
    get_end_text_for_split,
    get_end_text,
)

from mks_backend.services.fias_entity import (
    SUBJECT_SOCR_NAMES,
    CITY_SOCR_NAMES,
    LOCALITY_SOCR_NAMES,
    REMAINING_SOCR_NAMES,
    DISTRICT_SOCR_NAMES,
)

from mks_backend.models.fias import FIAS
from mks_backend.repositories.fias_entity.api import FIASAPIRepository


class FIASAPIService:

    def __init__(self):
        self.search_address = ''
        self.repo = FIASAPIRepository()

    def append_address_if_in_row_address(self, row_address: str, socr_name: str, suitable_addresses: list) -> None:
        if socr_name.lower() + self.search_address.lower() in row_address.lower():
            address = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name.lower() + self.search_address.lower() in address.lower():
                append_address(address, suitable_addresses)

    def split_fias(self, full_fias: str) -> FIAS:
        fias = FIAS()

        # Ошибка от стороннего fiasapi: 'Не найдено вариантов 'обл Московская''
        if full_fias == 'обл Московская':
            fias.subject = 'обл Московская'
            fias.aoid = 'd286798f-0849-4a7c-8e78-33c88dc964c6'
            return fias
        #

        end_text = get_end_text_for_split(full_fias)
        aoid = self.get_aoid(full_fias, end_text)

        if not aoid:
            return fias

        fias.aoid = aoid
        address_by_aoid = self.repo.get_details_by_aoid(aoid).json()
        fill_in_all_fields(address_by_aoid, fias)

        return fias

    def get_final_address(self, fias: FIAS) -> dict:
        end_text = get_end_text(fias)
        search_address = get_search_address(fias)
        aoid = self.get_aoid(search_address, end_text)
        return {
            'text': search_address,
            'aoid': aoid
        }

    def create_full_fias_hints(self, full_fias: str) -> list:
        number_responses = self.repo.suggests
        self.repo.suggests = 5

        fias_response = self.get_addresses_from_response(full_fias)

        self.repo.suggests = number_responses
        return fias_response

    def get_addresses_from_response(self, search_address: str) -> list:
        fias_response = self.get_fias_response(search_address)
        return extract_addresses(fias_response)

    def get_aoid(self, search_address: str, end_text: str) -> str:
        fias_response = self.get_final_response(search_address)

        if not fias_response:
            return ''

        full_resp = ''
        response = ''
        for resp in fias_response:
            if search_address == resp.get('text'):
                full_resp = resp
            elif search_address in resp.get('text'):
                response = resp

        if response:
            full_resp = response

        aoid = ''
        aoid_response = full_resp.get('aoid')
        address_by_aoid = self.repo.get_details_by_aoid(aoid_response).json()

        for row in address_by_aoid:
            if end_text in (row.get('shortname') + ' ' + row.get('formalname')):
                aoid = row.get('aoid')

        return aoid

    def get_final_response(self, search_address: str) -> list:
        number_responses = self.repo.suggests
        self.repo.suggests = 5

        fias_response = self.get_fias_response(search_address)

        self.repo.suggests = number_responses
        return fias_response.json()

    def get_fias_response(self, search_address: str) -> Response:
        return self.repo.get_fias_response(search_address)


def fill_in_all_fields(address_by_aoid: list, fias: FIAS) -> None:
    subject = ''
    district = ''
    city = ''
    locality = ''
    remaining_address = ''

    for row in address_by_aoid:
        subject_row = fill_in_field(row, SUBJECT_SOCR_NAMES)
        if subject_row:
            subject += subject_row + ', '

        district_row = fill_in_field(row, DISTRICT_SOCR_NAMES)
        if district_row:
            district += district_row + ', '

        city_row = fill_in_field(row, CITY_SOCR_NAMES)
        if city_row:
            city += city_row + ', '

        locality_row = fill_in_field(row, LOCALITY_SOCR_NAMES)
        if locality_row:
            locality += locality_row + ', '

        remaining_address_row = fill_in_field(row, REMAINING_SOCR_NAMES)
        if remaining_address_row:
            remaining_address += remaining_address_row + ', '

    if subject:
        fias.subject = subject.strip(', ')
    if district:
        fias.district = district.strip(', ')
    if city:
        fias.city = city.strip(', ')
    if locality:
        fias.locality = locality.strip(', ')
    if remaining_address:
        fias.remaining_address = remaining_address.strip(', ')


def fill_in_field(row: dict, socr_names: list) -> str:
    for socr_name in socr_names:
        if socr_name.strip(' ') == row.get('shortname'):
            return row.get('shortname') + ' ' + row.get('formalname')
