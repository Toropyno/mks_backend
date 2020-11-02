from mks_backend.models.fias import FIAS
from mks_backend.services.fias_entity import REMAINING_SOCR_NAMES
from mks_backend.services.fias_entity.address import FIASAPIService
from mks_backend.services.fias_entity.utils import append_address

from mks_backend.errors.fias_error import FIASError, fias_error_handler


class RemainingAddressService:

    def __init__(self):
        self.search_rem_address = ''
        self.remaining_addresses = set()
        self.service_api = FIASAPIService()

    @fias_error_handler
    def create_remaining_addresses_hints(self, fias: FIAS) -> set:
        if not (fias.city is not None or fias.locality is not None):
            raise FIASError('notFindCityLocality')

        self.remaining_addresses = set()

        if fias.remaining_address is None:
            fias.remaining_address = ''

        search_text = self.get_search_text(fias)
        addresses = self.service_api.get_addresses_from_response(search_text)
        if not addresses:
            raise FIASError('cannotFindAddress')

        for row_address in addresses:
            for socr in REMAINING_SOCR_NAMES:
                self.append_remaining_address_if_in_row_address(row_address, socr, fias.remaining_address)
        return self.remaining_addresses

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

        search_text += ', ' + remaining_address + ' ' + self.search_rem_address
        return search_text

    def append_remaining_address_if_in_row_address(self, row_address: str, socr_name: str,
                                                   remaining_address: str) -> None:

        address = self.get_remaining_address_by_socr_name(row_address, socr_name)

        if socr_name.lower() in address.lower() and self.search_rem_address.lower() in address.lower() \
                and address.replace(', ', '') not in remaining_address:
            append_address(address, self.remaining_addresses)

    def get_remaining_address_by_socr_name(self, row_address: str, socr_name: str) -> str:
        try:
            index_start = row_address.index(socr_name)
            remaining_address = row_address[index_start:]
        except ValueError:
            return ''

        if ', ' in remaining_address:
            remaining_address = remaining_address.split(', ')
            remaining_address = remaining_address[0]
        if socr_name.lower() in remaining_address.lower() and \
                self.search_rem_address.lower() in remaining_address.lower():
            try:
                index_end = row_address.index(socr_name, 0, -1) - 2
                index_start = row_address.rindex(', ', 0, index_end) + 2

                for socr in REMAINING_SOCR_NAMES:
                    if socr in row_address[index_start: index_end]:
                        address = row_address[index_start: index_end] + ', ' + remaining_address
                        remaining_address = address

            except ValueError:
                return remaining_address

        return remaining_address
