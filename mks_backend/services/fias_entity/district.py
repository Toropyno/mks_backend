from mks_backend.services.fias_entity.fias import (
    FIASService,
    get_reversed_addresses,
    get_by_socr_name,
    append_address,
)


class DistrictService:

    def __init__(self):
        self.search_district = ''
        self.districts = []
        self.service_FIAS = FIASService()

    def get_districts(self, subject: str) -> list:
        self.districts = []

        search_text = self.get_search_text(subject)
        addresses = self.service_FIAS.get_addresses_from_response(search_text)
        if not addresses:
            return []

        socr_names = ['р-н ', 'район ', 'у ']

        if subject is None:
            self.service_FIAS.search_address = self.search_district
            for row_address in addresses:
                for socr in socr_names:
                    self.service_FIAS.append_address_if_in_row_address(row_address, socr, self.districts)
            self.districts = get_reversed_addresses(self.districts)

        else:
            for row_address in addresses:
                for socr in socr_names:
                    self.append_district_if_in_row_address(row_address, socr, subject)

        return self.districts

    def get_search_text(self, subject: str) -> str:
        search_text = self.search_district
        if subject is not None:
            search_text = subject + ', ' + search_text
        return search_text

    def append_district_if_in_row_address(self, row_address: str, socr_name: str, subject: str) -> None:
        if (socr_name + self.search_district.lower() in row_address.lower()) and (
                subject.lower() in row_address.lower()):

            district = get_by_socr_name(row_address, socr_name)
            if socr_name + self.search_district.lower() in district.lower():
                append_address(district, self.districts)
