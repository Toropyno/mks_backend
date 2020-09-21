from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.location_type import LocationTypeSchema
from mks_backend.serializers.location_type import LocationTypeSerializer
from mks_backend.services.location_type import LocationTypeService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error


@view_defaults(renderer='json')
class LocationTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.service = LocationTypeService()
        self.serializer = LocationTypeSerializer()
        self.schema = LocationTypeSchema()

    @view_config(route_name='get_all_location_types')
    def get_all_location_types(self):
        location_types = self.service.get_all_location_types()
        return self.serializer.convert_list_to_json(location_types)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_location_type')
    def add_location_type(self):
        location_type_deserialized = self.schema.deserialize(self.request.json_body)

        location_type = self.serializer.convert_schema_to_object(location_type_deserialized)
        self.service.add_location_type(location_type)
        return {'id': location_type.location_types_id}

    @handle_db_error
    @view_config(route_name='delete_location_type')
    def delete_location_type(self):
        id = self.get_id()
        self.service.delete_location_type_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_location_type')
    def edit_location_type(self):
        location_type_deserialized = self.schema.deserialize(self.request.json_body)
        location_type_deserialized['id'] = self.request.matchdict['id']

        new_location_type = self.serializer.convert_schema_to_object(location_type_deserialized)
        self.service.update_location_type(new_location_type)
        return {'id': new_location_type.location_types_id}

    @handle_db_error
    @view_config(route_name='get_location_type')
    def get_location_type(self):
        id = self.get_id()
        location_type = self.service.get_location_type_by_id(id)
        return self.serializer.convert_object_to_json(location_type)

    def get_id(self):
        return int(self.request.matchdict['id'])
