import requests
from pyramid.request import Request
from pyramid.view import view_config, view_defaults
from requests import Response

from mks_backend.controllers.schemas.fias import FIASSchema
from mks_backend.serializers.fias.fias import FIASSerializer
from mks_backend.services.fias.fias import get_addresses_from_responce, get_by_socr_name, \
    get_address_ending_with_socr_name


@view_defaults(renderer='json')
class FIASController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = FIASSerializer()
        self.schema = FIASSchema()

    @view_config(route_name='get_fias')
    def get_fias(self):
        addresses = get_addresses_from_responce(self.get_fias_response())
        return addresses

    @view_config(route_name='get_subject')
    def get_subject(self):
        """
        Get subject: 'обл.', 'обл', 'Респ.', 'Респ', 'край '
        """
        addresses = get_addresses_from_responce(self.get_fias_response())
        subjects = []
        for row_address in addresses:
            self.append_subject_if_in_row_address(row_address, 'обл.', subjects)
            self.append_subject_if_in_row_address(row_address, 'обл ', subjects)
            self.append_subject_if_in_row_address(row_address, 'Респ.', subjects)
            self.append_subject_if_in_row_address(row_address, 'Респ ', subjects)
            self.append_subject_if_in_row_address(row_address, 'край ', subjects)
        return subjects

    @view_config(route_name='get_district')
    def get_district(self):
        """
        Get district: 'р-н ', 'район ', ' у '
        """
        addresses = get_addresses_from_responce(self.get_fias_response())
        districts = []

        subject = None
        # fias_deserialize = self.schema.deserialize(self.request.json_body)
        # fias = self.serializer.convert_schema_to_subject(fias_deserialize)
        # subject = fias.subject

        if subject is None:
            for row_address in addresses:
                self.append_address_if_in_row_address(row_address, 'р-н ', districts)
                self.append_address_if_in_row_address(row_address, 'район ', districts)
                self.append_address_if_in_row_address(row_address, ' у ', districts)
        else:
            for row_address in addresses:
                self.append_district_if_in_row_address(row_address, 'р-н ', districts, subject)
                self.append_district_if_in_row_address(row_address, 'район ', districts, subject)
                self.append_district_if_in_row_address(row_address, ' у ', districts, subject)
        return districts

    @view_config(route_name='get_city')
    def get_city(self):
        addresses = get_addresses_from_responce(self.get_fias_response())
        cities = []

        subject = None
        district = None
        # fias_deserialize = self.schema.deserialize(self.request.json_body)
        # fias = self.serializer.convert_schema_to_subject(fias_deserialize)
        # subject = fias.subject
        # district = fias.district

        if subject is None:
            for row_address in addresses:
                self.append_address_if_in_row_address(row_address, 'г.', cities)
                self.append_address_if_in_row_address(row_address, 'г ', cities)
                self.append_address_if_in_row_address(row_address, ' город ', cities)
            for address in cities:
                addresses = address.split(', ')
                addresses = sorted(addresses, reverse=True)
                print(addresses)

        elif district is None:
            for row_address in addresses:
                self.append_city_with_subject_district_if_in_row_address(row_address, 'г.', cities, subject)
                self.append_city_with_subject_district_if_in_row_address(row_address, 'г ', cities, subject)
                self.append_city_with_subject_district_if_in_row_address(row_address, ' город ', cities, subject)
        else:
            for row_address in addresses:
                self.append_city_if_in_row_address(row_address, 'г.', cities, subject, district)
                self.append_city_if_in_row_address(row_address, 'г ', cities, subject, district)
                self.append_city_if_in_row_address(row_address, ' город ', cities, subject, district)
        return cities

    def get_fias_response(self) -> Response:
        return requests.get(
            url='http://172.23.137.67/fiasapi/find/' + self.request.matchdict['text'] + '?suggests=150',
            headers={
                'Authorization': 'Basic dXNlcjoxMTExMTExMQ=='
            },
        )

    def get_by_AOID_response(self, aoid) -> Response:
        return requests.get(
            url='http://172.23.137.67/fiasapi/expand/' + aoid,
            headers={
                'Authorization': 'Basic dXNlcjoxMTExMTExMQ=='
            },
        )

    #   ---

    def append_subject_if_in_row_address(self, row_address, socr_name, subjects):
        if socr_name in row_address:
            subject = get_by_socr_name(row_address, socr_name)
            self.append_address_if_found(subject, subjects)

    # ---

    def append_district_if_in_row_address(self, row_address, socr_name, districts, subject):
        if (socr_name in row_address) and (subject in row_address):
            district = get_by_socr_name(row_address, socr_name)
            self.append_address_if_found(district, districts)

    # ---

    def append_city_with_subject_district_if_in_row_address(self, row_address, socr_name, cities, subject):
        if (socr_name in row_address) and (subject in row_address):
            city = get_address_ending_with_socr_name(row_address, socr_name)
            self.append_address_if_found(city, cities)

    def append_city_if_in_row_address(self, row_address, socr_name, cities, subject, district):
        if (socr_name in row_address) and (subject in row_address) and (district in row_address):
            city = get_by_socr_name(row_address, socr_name)
            self.append_address_if_found(city, cities)

    # ---

    def append_address_if_in_row_address(self, row_address, socr_name, suitable_addresses):
        if socr_name in row_address:
            address = get_address_ending_with_socr_name(row_address, socr_name)
            self.append_address_if_found(address, suitable_addresses)

    def append_address_if_found(self, address, suitable_addresses):
        if self.request.matchdict['text'].lower() in address.lower():
            if address not in suitable_addresses:
                suitable_addresses.append(address)
