from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.controllers.schemas.fias import FIASAPISchema
from mks_backend.serializers.fias.address import FIASAPISerializer
from mks_backend.serializers.fias.fias import FIASSerializer
from mks_backend.services.fias_entity.address import FIASAPIService

from mks_backend.errors.handle_controller_error import handle_colander_error


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
    @view_config(route_name='split_fields')
    def split_fields(self):
        full_fias_serialized = self.get_full_fias_serialized()
        split_full_fias = self.service.get_split_fields(full_fias_serialized)
        return self.serializer_FIAS.convert_object_to_json(split_full_fias)

    @handle_colander_error
    @view_config(route_name='create_final_address')
    def create_final_address(self):
        fias = self.controller_FIAS.get_fias_serialized()
        final_fias_address = self.service.create_final_address(fias)
        return final_fias_address

    @handle_colander_error
    @view_config(route_name='create_full_fias_hints')
    def create_full_fias_hints(self):
        full_fias = self.get_full_fias_serialized()
        return self.service.create_full_fias_hints(full_fias)

    @handle_colander_error
    @view_config(route_name='split_full_fias')
    def split_full_fias(self):
        split_full_fias = self.service.split_fias(self.get_full_fias_serialized())
        final_fias_address = self.serializer_FIAS.convert_object_to_json(split_full_fias)
        return final_fias_address

    def get_full_fias_serialized(self) -> str:
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_full_fias(fias_deserialized)
