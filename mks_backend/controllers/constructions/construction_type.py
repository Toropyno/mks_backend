from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.constructions import ConstructionTypeSchema
from mks_backend.serializers.constructions.construction_type import ConstructionTypeSerializer
from mks_backend.services.constructions.construction_type import ConstructionTypeService

from mks_backend.errors import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class ConstructionTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionTypeService()
        self.serializer = ConstructionTypeSerializer()
        self.schema = ConstructionTypeSchema()

    @view_config(route_name='get_all_construction_types')
    def get_all_construction_types(self):
        construction_types = self.service.get_all_construction_types()
        return self.serializer.convert_list_to_json(construction_types)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_construction_type')
    def add_construction_type(self):
        construction_type_deserialized = self.schema.deserialize(self.request.json_body)

        construction_type = self.serializer.convert_schema_to_object(construction_type_deserialized)
        self.service.add_construction_type(construction_type)
        return {'id': construction_type.construction_types_id}

    @handle_db_error
    @view_config(route_name='delete_construction_type')
    def delete_construction_type(self):
        id = self.get_id()
        self.service.delete_construction_type_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_construction_type')
    def edit_construction_type(self):
        construction_type_deserialized = self.schema.deserialize(self.request.json_body)
        construction_type_deserialized['id'] = self.get_id()

        new_construction_type = self.serializer.convert_schema_to_object(construction_type_deserialized)
        self.service.update_construction_type(new_construction_type)
        return {'id': new_construction_type.construction_types_id}

    @view_config(route_name='get_construction_type')
    def get_construction_type(self):
        id = self.get_id()
        construction_type = self.service.get_construction_type_by_id(id)
        return self.serializer.convert_object_to_json(construction_type)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
