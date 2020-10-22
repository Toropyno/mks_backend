from requests.models import Response

from mks_backend.errors.fias_error import fias_error_handler
from mks_backend.models.fias import FIAS


@fias_error_handler
def extract_addresses(response: Response) -> list:
    return [resp['text'] for resp in response.json()]


@fias_error_handler
def get_addresses_with_AOID(response: Response) -> list:
    return [{'text': resp['text'], 'AOID': resp['aoid']} for resp in response.json()]


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
    if fias.city is None and fias.locality is None:
        return ''

    if not fias.subject:
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
