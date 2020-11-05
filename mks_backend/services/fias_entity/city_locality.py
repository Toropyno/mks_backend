from mks_backend.models.fias import FIAS
from mks_backend.services.fias_entity import CITY_SOCR_NAMES, LOCALITY_SOCR_NAMES
from mks_backend.services.fias_entity.address import FIASAPIService

from mks_backend.services.fias_entity.utils import (
    get_by_socr_name,
    get_address_ending_with_socr_name,
    get_reversed_addresses,
    get_search_address
)

from mks_backend.errors.fias_error import fias_error_handler, FIASError


class CityLocalityService:

    def __init__(self):
        self.search_address = ''
        self.socr_names = []
        self.cities_or_localities = set()
        self.service_api = FIASAPIService()

    def set_city_socr_names(self) -> None:
        self.socr_names = CITY_SOCR_NAMES

    def set_locality_socr_names(self) -> None:
        self.socr_names = LOCALITY_SOCR_NAMES

    def get_search_text(self, fias: FIAS) -> str:
        search_text = self.search_address

        if fias.district is None and fias.subject is None:
            return search_text

        return get_search_address(fias) + ', ' + search_text

    @fias_error_handler
    def create_cities_or_localities_hints(self, fias: FIAS) -> list:
        self.cities_or_localities = set()

        search_text = self.get_search_text(fias)
        addresses = self.service_api.get_addresses_from_response(search_text)
        if not addresses:
            raise FIASError('cannotFindAddress')

        if fias.subject is None:
            self.service_api.search_address = self.search_address
            for row_address in addresses:
                for c_l in self.socr_names:
                    self.service_api.append_address_if_in_row_address(row_address, c_l, self.cities_or_localities)
            self.cities_or_localities = get_reversed_addresses(self.cities_or_localities)

        elif fias.district is None:
            for row_address in addresses:
                for c_l in self.socr_names:
                    self.append_with_subject_district_if_in_row_address(row_address, c_l, fias.subject)
            self.cities_or_localities = get_reversed_addresses(self.cities_or_localities)

        else:
            for row_address in addresses:
                for c_l in self.socr_names:
                    self.append_city_or_locality_if_in_row_address(row_address, c_l, fias)

        return list(self.cities_or_localities)

    def append_with_subject_district_if_in_row_address(self, row_address: str, socr_name: str, subject: str) -> None:
        if (socr_name.lower() + self.search_address.lower() in row_address.lower()) and (
                subject.lower() in row_address.lower()):

            c_or_l = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name.lower() + self.search_address.lower() in c_or_l.lower():
                self.cities_or_localities.add(c_or_l)

    def append_city_or_locality_if_in_row_address(self, row_address: str, socr_name: str, fias: FIAS) -> None:
        if (socr_name.lower() + self.search_address.lower() in row_address.lower()) and (
                fias.subject.lower() in row_address.lower()) and (
                fias.district.lower() in row_address.lower()):

            c_or_l = get_by_socr_name(row_address, socr_name)
            if socr_name.lower() + self.search_address.lower() in c_or_l.lower():
                self.cities_or_localities.add(c_or_l)
