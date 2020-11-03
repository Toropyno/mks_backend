from mks_backend.models.fias import FIAS
from mks_backend.services.fias_entity import REMAINING_SOCR_NAMES
from mks_backend.services.fias_entity.address import FIASAPIService

from mks_backend.errors.fias_error import FIASError, fias_error_handler


class RemainingAddressService:

    def __init__(self):
        self.search_rem_address = ''
        self.remaining_addresses = set()
        self.service_api = FIASAPIService()
        self.search_post_text = ''

    @fias_error_handler
    def create_remaining_addresses_hints(self, fias: FIAS) -> list:
        if not any((fias.city, fias.locality)):
            raise FIASError('notFindCityLocality')

        self.remaining_addresses = set()

        if fias.remaining_address is None:
            fias.remaining_address = ''

        self.search_post_text = self.get_search_text(fias).replace(', , ', ', ').strip()
        search_address = self.search_post_text + ' ' + self.search_rem_address

        addresses = self.service_api.get_addresses_from_response(search_address)
        if not addresses:
            raise FIASError('cannotFindAddress')

        for row_address in addresses:
            if self.search_post_text in row_address:
                for socr in REMAINING_SOCR_NAMES:
                    self.append_remaining_address_if_in_row_address(row_address, socr)

        return list(self.remaining_addresses)

    def get_search_text(self, fias: FIAS) -> str:
        city = fias.city
        locality = fias.locality
        subject = fias.subject
        district = fias.district
        remaining_address = fias.remaining_address

        if subject is None:
            subject = ''

        if district is None:
            district = ''

        search_text = subject + ', ' + district + ', '

        if locality is None:
            search_text += city
        elif city is None:
            search_text += locality
        else:
            search_text += city + ', ' + locality

        search_text += ', ' + remaining_address
        return search_text

    def append_remaining_address_if_in_row_address(self, row_address: str, socr_name: str) -> None:
        full_remaining_address = self.get_full_remaining_address(row_address, socr_name)

        if full_remaining_address:
            address = self.get_remaining_address(full_remaining_address, row_address, socr_name)
            self.append_remaining_addresses(address)

    def get_full_remaining_address(self, row_address: str, socr_name: str) -> str:
        if row_address.index(socr_name):
            index_start = row_address.index(socr_name)
            remaining_address = row_address[index_start:]
        else:
            remaining_address = ''
        return remaining_address

    def get_remaining_address(self, full_remaining_address: str, row_address: str, socr_name: str) -> str:
        first_remaining_address = ''
        remaining_address = full_remaining_address

        if ', ' in full_remaining_address:
            first_remaining_address = self.get_first_remaining_address(
                first_remaining_address, full_remaining_address, row_address
            )
        elif self.get_check(remaining_address.lower(), row_address):
            try:
                first_remaining_address = find_remaining_address(
                    first_remaining_address, remaining_address, row_address, socr_name
                )
            except ValueError:
                return full_remaining_address

        return first_remaining_address

    def get_first_remaining_address(self, first_remaining_address: str, full_remaining_address: str,
                                    row_address: str) -> str:
        remaining_address = full_remaining_address.split(', ')[0]

        if self.get_check(remaining_address.lower(), row_address):
            first_remaining_address = remaining_address

        return first_remaining_address

    def get_check(self, remaining_address: str, row_address: str) -> bool:
        return self.search_rem_address.lower() in remaining_address.lower() and self.search_post_text in row_address

    def append_remaining_addresses(self, address: str) -> None:
        if address:
            self.remaining_addresses.add(address)


def find_remaining_address(first_remaining_address: str, remaining_address: str, row_address: str,
                           socr_name: str) -> str:
    index_end = row_address.index(socr_name, 0, -1) - 2
    index_start = row_address.rindex(', ', 0, index_end) + 2

    for socr in REMAINING_SOCR_NAMES:
        if socr in row_address[index_start: index_end]:
            first_remaining_address = row_address[index_start: index_end] + ', ' + remaining_address

    if not first_remaining_address:
        first_remaining_address = remaining_address

    return first_remaining_address
