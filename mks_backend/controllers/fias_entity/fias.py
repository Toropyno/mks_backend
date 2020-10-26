from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.schemas.fias import FIASSchema
from mks_backend.errors.fias_error import get_addition_fias_error_dict, get_remaining_address_error_dict
from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
from mks_backend.models.fias import FIAS
from mks_backend.serializers.fias import FIASSerializer
from mks_backend.services.fias_entity.fias import FIASService


@view_defaults(renderer='json')
class FIASController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = FIASSchema()
        self.service = FIASService()
        self.serializer = FIASSerializer()

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_fias')
    def add_fias(self):
        fias = self.get_fias_serialized()
        fias = self.service.add_address_fias(fias)
        if not fias:
            return get_addition_fias_error_dict()
        return self.serializer.convert_object_to_json(fias)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='get_split_full_fias')
    def get_split_full_fias(self):
        full_fias = self.get_full_fias_serialized()
        split_full_fias = self.service.get_split_full_fias(full_fias)
        if not split_full_fias:
            return get_remaining_address_error_dict()
        return self.serializer.convert_object_to_json(split_full_fias)

    @handle_db_error
    @view_config(route_name='get_fias')
    def get_fias(self):
        id = self.get_id()
        fias = self.service.get_fias_by_id(id)
        return self.serializer.convert_object_to_json(fias)

    @handle_db_error
    @view_config(route_name='get_all_fiases')
    def get_all_fiases(self):
        fiases = self.service.get_all_fiases()
        return self.serializer.convert_list_to_json(fiases)

    def get_fias_serialized(self) -> FIAS:
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_schema_to_object(fias_deserialized)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])

    def get_full_fias_serialized(self) -> str:
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_full_fias(fias_deserialized)
