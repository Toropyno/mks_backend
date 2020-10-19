from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.controllers.schemas.construction_category import ConstructionCategorySchema
from mks_backend.serializers.construction_category import ConstructionCategorySerializer
from mks_backend.services.construction_category import ConstructionCategoryService

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


class ConstructionCategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionCategorySerializer()
        self.service = ConstructionCategoryService()
        self.schema = ConstructionCategorySchema()

    @view_config(route_name='get_all_construction_categories', renderer='json')
    def get_all_construction_categories(self):
        construction_categories = self.service.get_all_construction_categories()
        return self.serializer.convert_list_to_json(construction_categories)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_construction_category', renderer='json')
    def add_construction_category(self):
        construction_categories_deserialized = self.schema.deserialize(self.request.json_body)

        construction_category = self.service.convert_schema_to_object(construction_categories_deserialized)
        self.service.add_construction_category(construction_category)

        return {'id': construction_category.construction_categories_id}

    @view_config(route_name='get_construction_category', renderer='json')
    def get_construction_category(self):
        id = int(self.request.matchdict['id'])
        construction_category = self.service.get_construction_category_by_id(id)
        return self.serializer.convert_object_to_json(construction_category)

    @view_config(route_name='delete_construction_category', renderer='json')
    def delete_construction_category(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_category_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_construction_category', renderer='json')
    def edit_construction_category(self):
        construction_categories_deserialized = self.schema.deserialize(self.request.json_body)
        construction_categories_deserialized['id'] = int(self.request.matchdict['id'])

        construction_category = self.service.convert_schema_to_object(construction_categories_deserialized)
        self.service.update_construction_category(construction_category)
        return {'id': id}
