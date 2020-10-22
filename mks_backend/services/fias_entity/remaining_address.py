from mks_backend.models.fias import FIAS
from mks_backend.services.fias_entity.fias import FIASService, append_address


class RemainingAddressService:

    def __init__(self):
        self.search_rem_address = ''
        self.remaining_addresses = []
        self.service_FIAS = FIASService()

    def get_remaining_addresses(self, fias: FIAS) -> list:
        self.remaining_addresses = []

        search_text = self.get_search_text(fias)
        addresses = self.service_FIAS.get_addresses_from_response(search_text)
        if not addresses:
            return []

        socr_names = ['ул ', 'ул. ', 'пер ', 'пер. ', 'ш ', 'ш. ', 'кв-л ', 'тер ', 'тер. ', 'мкр ', 'мкр. ', 'пр-кт ',
                      'б-р ', 'б-р. ', 'проезд ', 'проезд. ', 'туп ', 'туп. ', 'пл ', 'пл. ']

        for row_address in addresses:
            for socr in socr_names:
                self.append_remaining_address_if_in_row_address(row_address, socr)
        return self.remaining_addresses

    def get_search_text(self, fias: FIAS) -> str:
        city = fias.city
        locality = fias.locality
        subject = fias.subject
        district = fias.district

        if district is None:
            district = ''

        search_text = subject + ', ' + district + ', '

        if locality is None:
            search_text += city
        elif city is None:
            search_text += locality
        else:
            search_text += city + ', ' + locality

        search_text += ', ' + self.search_rem_address
        return search_text

    def append_remaining_address_if_in_row_address(self, row_address: str, socr_name: str) -> None:
        address = get_remaining_address_by_socr_name(row_address, socr_name)
        if address:
            if socr_name + self.search_rem_address.lower() in address.lower():
                append_address(address, self.remaining_addresses)


def get_remaining_address_by_socr_name(row_address: str, socr_name: str) -> str:
    try:
        return row_address[row_address.index(socr_name):]
    except ValueError:
        return ''
