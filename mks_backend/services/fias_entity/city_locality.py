from mks_backend.services.fias_entity.fias import (
    get_address_ending_with_socr_name,
    append_address,
    get_by_socr_name,
    get_reversed_address,
    FIASService,
)


class CityLocalityService:

    def __init__(self):
        self.search_address = ''
        self.socr_names = []
        self.service_fias = FIASService()

    def set_search_address(self, search_address):
        self.search_address = search_address

    def set_socr_names(self, socr_names):
        self.socr_names = socr_names

    def get_search_text(self, district, subject):
        search_text = self.search_address
        if district is not None:
            search_text = subject + ', ' + district + ', ' + search_text
        elif subject is not None:
            search_text = subject + ', ' + search_text
        return search_text

    def get_cities_or_localities(self, addresses, district, subject):
        cities_or_localities = []
        if subject is None:
            self.service_fias.set_search_address(self.search_address)
            for row_address in addresses:
                for c_l in self.socr_names:
                    self.service_fias.append_address_if_in_row_address(row_address, c_l, cities_or_localities)
            cities_or_localities = get_reversed_address(cities_or_localities)
        elif district is None:
            for row_address in addresses:
                for c_l in self.socr_names:
                    self.append_city_or_locality_with_subject_district_if_in_row_address(
                        row_address, c_l, cities_or_localities, subject
                    )
            cities_or_localities = get_reversed_address(cities_or_localities)
        else:
            for row_address in addresses:
                for c_l in self.socr_names:
                    self.append_city_if_in_row_address(row_address, c_l, cities_or_localities, subject, district)
        return cities_or_localities

    def append_city_or_locality_with_subject_district_if_in_row_address(self, row_address, socr_name, cities_localities,
                                                                        subject):
        if (socr_name in row_address) and (subject in row_address):
            c_or_l = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in c_or_l.lower():
                append_address(c_or_l, cities_localities)

    def append_city_if_in_row_address(self, row_address, socr_name, cities_localities, subject, district):
        if (socr_name in row_address) and (subject in row_address) and (district in row_address):
            c_or_l = get_by_socr_name(row_address, socr_name)
            if socr_name + self.search_address.lower() in c_or_l.lower():
                append_address(c_or_l, cities_localities)
