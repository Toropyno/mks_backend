import requests
from pyramid.request import Request
from pyramid.view import view_config, view_defaults
from requests import Response

from mks_backend.controllers.schemas.fias import FIASSchema
from mks_backend.serializers.fias.fias import FIASSerializer
from mks_backend.services.fias.fias import get_addresses_from_responce, get_by_socr_name


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

    def get_fias_response(self) -> Response:
        return requests.get(
            url='http://172.23.137.67/fiasapi/find/' + self.request.matchdict['text'] + '?suggests=15',
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