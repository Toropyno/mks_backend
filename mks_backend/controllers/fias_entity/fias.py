import requests
from pyramid.request import Request
from pyramid.view import view_config, view_defaults
from requests import Response

from mks_backend.controllers.schemas.fias import FIASSchema
from mks_backend.serializers.fias import FIASSerializer
from mks_backend.services.fias_entity.fias import (
    get_addresses_from_response,
    FIASService,
)


@view_defaults(renderer='json')
class FIASController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = FIASSerializer()
        self.schema = FIASSchema()
        self.service = FIASService()

    @view_config(route_name='get_fias')
    def get_fias(self):
        search_address = self.request.matchdict['text']
        return get_addresses_from_response(get_fias_response(search_address))

    def get_fias_serialized(self):
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_schema_to_object(fias_deserialized)


def get_fias_response(search_text) -> Response:
    return requests.get(
        url='http://172.23.137.67/fiasapi/find/' + search_text + '?suggests=15',
        headers={
            'Authorization': 'Basic dXNlcjoxMTExMTExMQ=='
        },
    )


def get_by_AOID_response(aoid) -> Response:
    return requests.get(
        url='http://172.23.137.67/fiasapi/expand/' + aoid,
        headers={
            'Authorization': 'Basic dXNlcjoxMTExMTExMQ=='
        },
    )
