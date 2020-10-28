from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.controllers.schemas.fias import FIASAPISchema
from mks_backend.errors.fias_error import get_remaining_address_error_dict, get_addition_fias_error_dict
from mks_backend.errors.handle_controller_error import handle_colander_error
from mks_backend.serializers.fias.api import FIASAPISerializer
from mks_backend.serializers.fias.fias import FIASSerializer
from mks_backend.services.fias_entity.api import FIASAPIService


@view_defaults(renderer='json')
class FIASAPIController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = FIASAPISchema()
        self.service = FIASAPIService()
        self.serializer = FIASAPISerializer()
        self.controller_FIAS = FIASController(self.request)
        self.serializer_FIAS = FIASSerializer()

    @handle_colander_error
    @view_config(route_name='get_final_address')
    def get_final_address(self):
        fias = self.controller_FIAS.get_fias_serialized()
        final_fias_address = self.service.get_final_address(fias)
        if not final_fias_address:
            return get_remaining_address_error_dict()
        return {'final_address': final_fias_address}

    @handle_colander_error
    @view_config(route_name='create_full_fias_hints')
    def create_full_fias_hints(self):
        full_fias = self.get_full_fias_serialized()
        return self.service.create_full_fias_hints(full_fias)

    @handle_colander_error
    @view_config(route_name='split_full_fias')
    def split_full_fias(self):
        full_fias = self.get_full_fias_serialized()
        split_full_fias = self.service.split_full_fias(full_fias)
        if not split_full_fias:
            return get_remaining_address_error_dict()
        return self.serializer_FIAS.convert_object_to_json(split_full_fias)

    def get_full_fias_serialized(self) -> str:
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_full_fias(fias_deserialized)
