from mks_backend.services.fias_entity.fias import (
    FIASService, append_address,
)


class RemainingAddressService:

    def __init__(self):
        self.text = ''
        self.service_fias = FIASService()

    def set_text(self, text):
        self.text = text

    def get_search_text(self, address):
        search_text = self.text

        city = address.get('city')
        locality = address.get('locality')
        subject = address.get('subject')
        district = address.get('district')

        if district is None:
            district = ''
        if locality is None:
            search_text = subject + ', ' + district + ', ' + city + ', ' + self.text
        elif city is None:
            search_text = subject + ', ' + district + ', ' + locality + ', ' + self.text
        else:
            search_text = subject + ', ' + district + ', ' + city + ', ' + locality + ', ' + self.text

        return search_text

    def get_streets_houses(self, addresses):
        streets_houses = []
        socr_names = ['ул ', 'ул. ', 'пер ', 'пер. ', 'ш ', 'ш. ', 'кв-л ', 'тер ', ' тер. ', 'мкр ', 'мкр. ', 'пр-кт ']
        for row_address in addresses:
            for socr in socr_names:
                self.append_streets_houses_if_in_row_address(row_address, socr, streets_houses)
        return streets_houses

    def append_streets_houses_if_in_row_address(self, row_address, socr_name, streets_houses):
        address = get_streets_houses_by_socr_name(row_address, socr_name)
        if address:
            if socr_name + self.text.lower() in address.lower():
                append_address(address, streets_houses)


def get_streets_houses_by_socr_name(row_address, socr_name):
    try:
        return row_address[row_address.index(socr_name):]
    except ValueError:
        return ''
