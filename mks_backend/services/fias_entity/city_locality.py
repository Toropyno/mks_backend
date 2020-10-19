from mks_backend.models.fias import FIAS
from mks_backend.services.fias_entity.fias import (
    get_address_ending_with_socr_name,
    append_address,
    get_by_socr_name,
    get_reversed_addresses,
    FIASService,
)


class CityLocalityService:

    def __init__(self):
        self.search_address = ''
        self.socr_names = []
        self.cities_or_localities = []
        self.service_fias = FIASService()

    def set_search_address(self, search_address: str) -> None:
        self.search_address = search_address

    def set_socr_names(self, socr_names: list) -> None:
        self.socr_names = socr_names

    def get_search_text(self, fias: FIAS) -> str:
        search_text = self.search_address
        subject = fias.subject
        district = fias.district

        if district is not None:
            search_text = subject + ', ' + district + ', ' + search_text
        elif subject is not None:
            search_text = subject + ', ' + search_text
        return search_text

    def get_cities_or_localities(self, addresses: list, fias: FIAS) -> list:
        self.cities_or_localities = []

        if fias.subject is None:
            self.service_fias.set_search_address(self.search_address)
            for row_address in addresses:
                for c_l in self.socr_names:
                    self.service_fias.append_address_if_in_row_address(row_address, c_l, self.cities_or_localities)
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

        return self.cities_or_localities

    def append_with_subject_district_if_in_row_address(self, row_address: str, socr_name: str, subject: str) -> None:
        if (socr_name + self.search_address.lower() in row_address.lower()) and (subject.lower() in row_address.lower()):
            c_or_l = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in c_or_l.lower():
                append_address(c_or_l, self.cities_or_localities)

    def append_city_or_locality_if_in_row_address(self, row_address: str, socr_name: str, fias: FIAS) -> None:
        if (socr_name + self.search_address.lower() in row_address.lower()) and (
                fias.subject.lower() in row_address.lower()) and (fias.district.lower() in row_address.lower()):
            c_or_l = get_by_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in c_or_l.lower():
                append_address(c_or_l, self.cities_or_localities)
