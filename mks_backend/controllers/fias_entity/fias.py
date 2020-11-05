from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.schemas.fias import FIASSchema
from mks_backend.models.fias import FIAS
from mks_backend.serializers.fias.fias import FIASSerializer
from mks_backend.services.fias_entity.fias import FIASService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error


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
        return self.serializer.convert_object_to_json(fias)

    @handle_db_error
    @view_config(route_name='get_fias')
    def get_fias_by_id(self):
        id = self.get_id()
        fias = self.service.get_fias_by_id(id)
        return self.serializer.convert_object_to_json(fias)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])

    def get_fias_serialized(self) -> FIAS:
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_schema_to_object(fias_deserialized)
