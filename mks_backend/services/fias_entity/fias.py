class FIASService:

    def __init__(self):
        self.search_address = ''

    def set_search_address(self, search_address):
        self.search_address = search_address

    def append_address_if_in_row_address(self, row_address, socr_name, suitable_addresses):
        if socr_name in row_address:
            address = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in address.lower():
                append_address(address, suitable_addresses)


def get_addresses_from_response(response) -> list:
    try:
        return [rr['text'] for rr in response.json()]
    except TypeError:
        return [
            {'status': 403},
            {
                'json_body': {
                    'code': 'text_short',
                    'message': 'The text is too short'
                }
            }
        ]


def get_by_socr_name(row_address, socr_name):
    start_index = row_address.index(socr_name)
    try:
        end_index = row_address.index(', ', start_index, -1)
        address_by_socr_name = row_address[start_index:end_index]
    except ValueError:
        address_by_socr_name = row_address[start_index:]
    return address_by_socr_name


def get_address_ending_with_socr_name(row_address, socr_name):
    try:
        index_socr_name = row_address.index(socr_name, 0, -1)
        end_index = row_address.index(', ', index_socr_name, -1)
        address = row_address[0:end_index]
    except ValueError:
        address = row_address
    return address


def get_reversed_address(addresses):
    reversed_addresses = []
    for address in addresses:
        gluing = ''
        address_split_reversed = address.split(', ')[::-1]
        for addr in address_split_reversed:
            gluing += addr + ', '
        reversed_addresses.append(gluing.strip(', '))
    return reversed_addresses


def append_address(address, suitable_addresses):
    if address not in suitable_addresses:
        suitable_addresses.append(address)
