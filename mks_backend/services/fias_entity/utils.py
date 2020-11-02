from requests.models import Response

from mks_backend.errors.fias_error import fias_error_handler
from mks_backend.models.fias import FIAS


@fias_error_handler
def extract_addresses(response: Response) -> list:
    return [resp.get('text') for resp in response.json()]


@fias_error_handler
def extract_addresses_with_aoid(response: Response) -> list:
    return [{'text': resp.get('text'), 'aoid': resp.get('aoid')} for resp in response.json()]


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
        gluing = turn_over_address(address)
        reversed_addresses.append(gluing)
    return reversed_addresses


def turn_over_address(address: str) -> str:
    gluing = ''
    address_split_reversed = address.split(', ')[::-1]
    for addr in address_split_reversed:
        gluing += addr + ', '
    return gluing.strip(', ')


def get_search_address(fias: FIAS) -> str:
    search_address = ''

    if fias.subject:
        search_address = fias.subject
    if fias.district:
        search_address += ', ' + fias.district
    if fias.city:
        search_address += ', ' + fias.city
    if fias.locality:
        search_address += ', ' + fias.locality
    if fias.remaining_address:
        search_address += ', ' + fias.remaining_address

    return search_address


def get_end_text_for_split(full_fias: str) -> str:
    try:
        start_index = full_fias.rindex(', ') + 2
        end_text = full_fias[start_index:len(full_fias)]
    except ValueError:
        end_text = full_fias[:]
    return end_text


def get_end_text(fias: FIAS) -> str:
    end_text = ''
    if fias.remaining_address:
        end_text = get_end_text_for_split(fias.remaining_address)
    elif fias.locality:
        end_text = get_end_text_for_split(fias.locality)
    elif fias.city:
        end_text = get_end_text_for_split(fias.city)
    elif fias.district:
        end_text = get_end_text_for_split(fias.district)
    elif fias.subject:
        end_text = get_end_text_for_split(fias.subject)
    return end_text
