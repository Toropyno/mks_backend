from mks_backend.services.fias_entity.fias import (
    FIASService,
    get_reversed_address,
    get_by_socr_name,
    append_address,
)


class DistrictService:

    def __init__(self):
        self.search_district = ''
        self.service_fias = FIASService()

    def set_search_district(self, search_district):
        self.search_district = search_district

    def get_districts(self, addresses, subject):
        districts = []
        if subject is None:
            self.service_fias.set_search_address(self.search_district)
            for row_address in addresses:
                self.service_fias.append_address_if_in_row_address(row_address, 'р-н ', districts)
                self.service_fias.append_address_if_in_row_address(row_address, 'район ', districts)
                self.service_fias.append_address_if_in_row_address(row_address, ' у ', districts)
            districts = get_reversed_address(districts)
        else:
            for row_address in addresses:
                self.append_district_if_in_row_address(row_address, 'р-н ', districts, subject)
                self.append_district_if_in_row_address(row_address, 'район ', districts, subject)
                self.append_district_if_in_row_address(row_address, ' у ', districts, subject)
        return districts

    def append_district_if_in_row_address(self, row_address, socr_name, districts, subject):
        if (socr_name in row_address) and (subject in row_address):
            district = get_by_socr_name(row_address, socr_name)
            if socr_name + self.search_district.lower() in district.lower():
                append_address(district, districts)
