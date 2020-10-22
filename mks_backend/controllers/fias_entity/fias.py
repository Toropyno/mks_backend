from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.fias import FIASSchema
from mks_backend.models.fias import FIAS
from mks_backend.serializers.fias import FIASSerializer
from mks_backend.services.fias_entity.fias import FIASService, get_search_address


@view_defaults(renderer='json')
class FIASController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = FIASSchema()
        self.service = FIASService()
        self.serializer = FIASSerializer()

    @view_config(route_name='get_fias')
    def get_fias(self):
        return self.service.get_addresses_from_response(self.request.matchdict['text'])

    @view_config(route_name='add_fias')
    def add_fias(self):
        fias = self.get_fias_serialized()

        search_address = get_search_address(fias)
        if search_address == '':
            return [
                {'status': 403},
                {
                    'json_body': {
                        'code': 'not_full_address',
                        'message': 'Адрес заполнен не полностью'
                    }
                }
            ]
        fias.aoid = self.service.get_AOID(search_address)

        self.service.add_fias(fias)

    @view_config(route_name='get_final_fias_address')
    def get_final_fias_address(self):
        fias = self.get_fias_serialized()
        search_address = get_search_address(fias)

        return self.service.get_final_fias_address(search_address)

    def get_fias_serialized(self) -> FIAS:
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_schema_to_object(fias_deserialized)
