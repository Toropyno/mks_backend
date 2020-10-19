from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.controllers.schemas.construction_subcategory import ConstructionSubcategorySchema
from mks_backend.serializers.construction_subcategory import ConstructionSubcategorySerializer
from mks_backend.services.construction_subcategory import ConstructionSubcategoryService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error


class ConstructionSubcategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionSubcategorySerializer()
        self.service = ConstructionSubcategoryService()
        self.schema = ConstructionSubcategorySchema()

    @view_config(route_name='get_all_construction_subcategories', renderer='json')
    def get_all_construction_subcategories(self):
        construction_subcategories = self.service.get_all_construction_subcategories()
        return self.serializer.convert_list_to_json(construction_subcategories)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_construction_subcategory', renderer='json')
    def add_construction_subcategory(self):
        construction_subcategories_deserialized = self.schema.deserialize(self.request.json_body)
        construction_subcategory = self.serializer.convert_schema_to_object(construction_subcategories_deserialized)

        self.service.add_construction_subcategory(construction_subcategory)
        return {'id': construction_subcategory.construction_subcategories_id}

    @view_config(route_name='get_construction_subcategory', renderer='json')
    def get_construction_subcategory(self):
        id = int(self.request.matchdict['id'])
        construction_subcategory = self.service.get_construction_subcategory_by_id(id)
        return self.serializer.convert_object_to_json(construction_subcategory)

    @view_config(route_name='delete_construction_subcategory', renderer='json')
    def delete_construction_subcategory(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_subcategory_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_construction_subcategory', renderer='json')
    def edit_construction_subcategory(self):
        construction_subcategories_deserialized = self.schema.deserialize(self.request.json_body)
        construction_subcategories_deserialized['id'] = int(self.request.matchdict['id'])

        construction_subcategory = self.serializer.convert_schema_to_object(construction_subcategories_deserialized)
        self.service.update_construction_subcategory(construction_subcategory)
        return {'id': id}
