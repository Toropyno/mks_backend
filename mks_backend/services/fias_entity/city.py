from mks_backend.services.fias_entity.fias import (
    get_address_ending_with_socr_name,
    append_address,
    get_by_socr_name,
    get_reversed_address,
    FIASService,
)


class CityOrLocalityService:

    def __init__(self):
        self.text = ''
        self.city_or_locality = []
        self.service_fias = FIASService()

    def set_text(self, text):
        self.text = text

    def set_city_or_locality(self, set_city_or_locality):
        self.city_or_locality = set_city_or_locality

    def get_cities_or_localities(self, addresses, district, subject, text):
        cities = []
        if subject is None:
            self.service_fias.set_text(text)
            for row_address in addresses:
                for c_l in self.city_or_locality:
                    self.service_fias.append_address_if_in_row_address(row_address, c_l, cities)
            cities = get_reversed_address(cities)
        elif district is None:
            for row_address in addresses:
                for c_l in self.city_or_locality:
                    self.append_city_with_subject_district_if_in_row_address(
                        row_address, c_l, cities, cities, subject
                    )
            cities = get_reversed_address(cities)
        else:
            for row_address in addresses:
                for c_l in self.city_or_locality:
                    self.append_city_if_in_row_address(row_address, c_l, cities, subject, district)
        return cities

    def append_city_with_subject_district_if_in_row_address(self, row_address, socr_name, cities, subject):
        if (socr_name in row_address) and (subject in row_address):
            city = get_address_ending_with_socr_name(row_address, socr_name)
            if socr_name + self.text.lower() in city.lower():
                append_address(city, cities)

    def append_city_if_in_row_address(self, row_address, socr_name, cities, subject, district):
        if (socr_name in row_address) and (subject in row_address) and (district in row_address):
            city = get_by_socr_name(row_address, socr_name)
            if socr_name + self.text.lower() in city.lower():
                append_address(city, cities)
