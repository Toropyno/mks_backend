def get_addresses_from_responce(responce) -> list:
    try:
        return [rr['text'] for rr in responce.json()]
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
