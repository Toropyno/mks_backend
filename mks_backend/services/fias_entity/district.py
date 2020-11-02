from mks_backend.services.fias_entity import DISTRICT_SOCR_NAMES
from mks_backend.services.fias_entity.address import FIASAPIService

from mks_backend.services.fias_entity.utils import (
    get_by_socr_name,
    append_address,
    get_reversed_addresses
)

from mks_backend.errors.fias_error import fias_error_handler, FIASError


class DistrictService:

    def __init__(self):
        self.search_district = ''
        self.districts = set()
        self.service_api = FIASAPIService()

    @fias_error_handler
    def create_districts_hints(self, subject: str) -> set:
        self.districts = set()

        search_text = self.get_search_text(subject)
        addresses = self.service_api.get_addresses_from_response(search_text)
        if not addresses:
            raise FIASError('cannotFindAddress')

        if subject is None:
            self.service_api.search_address = self.search_district
            for row_address in addresses:
                for socr in DISTRICT_SOCR_NAMES:
                    self.service_api.append_address_if_in_row_address(row_address, socr, self.districts)
            self.districts = get_reversed_addresses(self.districts)

        else:
            for row_address in addresses:
                for socr in DISTRICT_SOCR_NAMES:
                    self.append_district_if_in_row_address(row_address, socr, subject)

        return self.districts

    def get_search_text(self, subject: str) -> str:
        search_text = self.search_district
        if subject is not None:
            search_text = subject + ', ' + search_text
        return search_text

    def append_district_if_in_row_address(self, row_address: str, socr_name: str, subject: str) -> None:
        if (socr_name.lower() + self.search_district.lower() in row_address.lower()) and (
                subject.lower() in row_address.lower()):

            district = get_by_socr_name(row_address, socr_name)
            if socr_name.lower() + self.search_district.lower() in district.lower():
                append_address(district, self.districts)
