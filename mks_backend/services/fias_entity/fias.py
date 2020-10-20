from requests import Response


class FIASService:

    def __init__(self):
        self.search_address = ''

    def append_address_if_in_row_address(self, row_address: str, socr_name: str, suitable_addresses: list) -> None:
        if socr_name + self.search_address.lower() in row_address.lower():
            address = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in address.lower():
                append_address(address, suitable_addresses)


def get_addresses_from_response(response: Response) -> list:
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
