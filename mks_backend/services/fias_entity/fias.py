from requests import Response

from mks_backend.models.fias import FIAS
from mks_backend.repositories.fias_entity.api import FIASAPIRepository


class FIASService:

    def __init__(self):
        self.search_address = ''
        self.repository = FIASAPIRepository()

    def append_address_if_in_row_address(self, row_address: str, socr_name: str, suitable_addresses: list) -> None:
        if socr_name + self.search_address.lower() in row_address.lower():
            address = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in address.lower():
                append_address(address, suitable_addresses)

    def get_fias_response(self, search_text: str) -> Response:
        return self.repository.get_fias_response(search_text)

    def get_final_fias_response(self, search_text: str) -> Response:
        number_responses = self.repository.number_responses
        self.repository.number_responses = 1
        fias_response = self.get_fias_response(search_text)
        self.repository.number_responses = number_responses
        return fias_response

    def get_AOID(self, search_address: str) -> str:
        fias_response = self.get_final_fias_address(search_address).get('AOID')
        return fias_response.get('AOID')

    def get_final_fias_address(self, search_address: str) -> dict:
        fias_response = self.get_final_fias_response(search_address)
        return self.get_addresses_with_AOID(fias_response)[0]

    def get_addresses_from_response(self, response: Response) -> list:
        try:
            return [rr['text'] for rr in response.json()]
        except TypeError:
            return [
                {'status': 403},
                {
                    'json_body': {
                        'code': 'text_short',
                        'message': 'Слишком короткий текст'
                    }
                }
            ]

    def get_addresses_with_AOID(self, response: Response) -> list:
        try:
            return [{'text': rr['text'], 'AOID': rr['aoid']} for rr in response.json()]
        except TypeError:
            return [
                {'status': 403},
                {
                    'json_body': {
                        'code': 'text_short',
                        'message': 'Слишком короткий текст'
                    }
                }
            ]


def get_by_socr_name(row_address: str, socr_name: str) -> str:
    start_index = row_address.index(socr_name)
    try:
        end_index = row_address.index(', ', start_index, -1)
        address_by_socr_name = row_address[start_index:end_index]
    except ValueError:
        address_by_socr_name = row_address[start_index:]
    return address_by_socr_name


def get_address_ending_with_socr_name(row_address: str, socr_name: str) -> str:
    try:
        index_socr_name = row_address.index(socr_name, 0, -1)
        end_index = row_address.index(', ', index_socr_name, -1)
        address = row_address[0:end_index]
    except ValueError:
        address = row_address
    return address


def append_address(address: str, suitable_addresses: list) -> None:
    if address not in suitable_addresses:
        suitable_addresses.append(address)


def get_reversed_addresses(addresses: list) -> list:
    reversed_addresses = []
    for address in addresses:
        gluing = ''
        address_split_reversed = address.split(', ')[::-1]
        for addr in address_split_reversed:
            gluing += addr + ', '
        reversed_addresses.append(gluing.strip(', '))
    return reversed_addresses


def get_search_address(fias: FIAS) -> str:
    if fias.city is not None or fias.locality is not None:
        return ''

    if fias.subject:
        fias.subject = ''
    if not fias.district:
        fias.district = ''
    if not fias.city:
        fias.city = ''
    if not fias.locality:
        fias.locality = ''
    if not fias.remaining_address:
        fias.remaining_address = ''
    search_address = fias.subject + ', ' + fias.district + ', ' + fias.city + ', ' + fias.locality + ', ' + fias.remaining_address
    return search_address
