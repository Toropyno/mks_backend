from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.fias import FIASSchema
from mks_backend.models.fias import FIAS
from mks_backend.repositories.fias_entity.api import get_fias_response
from mks_backend.serializers.fias import FIASSerializer
from mks_backend.services.fias_entity.fias import get_addresses_from_response, FIASService


@view_defaults(renderer='json')
class FIASController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = FIASSchema()
        self.service = FIASService()
        self.serializer = FIASSerializer()

    @view_config(route_name='get_fias')
    def get_fias(self):
        search_address = self.request.matchdict['text']
        return get_addresses_from_response(get_fias_response(search_address))

    def get_fias_serialized(self) -> FIAS:
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_schema_to_object(fias_deserialized)



