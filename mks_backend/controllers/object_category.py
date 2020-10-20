from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.controllers.schemas.object_category import ObjectCategorySchema
from mks_backend.serializers.object_category import ObjectCategorySerializer
from mks_backend.services.object_category import ObjectCategoryService

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


class ObjectCategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ObjectCategoryService()
        self.serializer = ObjectCategorySerializer()
        self.schema = ObjectCategorySchema()

    @view_config(route_name='get_all_object_categories', renderer='json')
    def get_all_object_categories(self):
        object_categories = self.service.get_all_object_categories()
        return self.serializer.convert_list_to_json(object_categories)

    @view_config(route_name='get_object_category', renderer='json')
    def get_object_category(self):
        id = int(self.request.matchdict['id'])
        object_category = self.service.get_object_category_by_id(id)
        return self.serializer.convert_object_to_json(object_category)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_object_category', renderer='json')
    def add_object_category(self):
        object_category_deserialized = self.schema.deserialize(self.request.json_body)
        object_category = self.serializer.convert_schema_to_object(object_category_deserialized)

        self.service.add_object_category(object_category)
        return {'id': object_category.object_categories_id}

    @view_config(route_name='delete_object_category', renderer='json')
    def delete_construction_object(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_object_category_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_object_category', request_method='PUT', renderer='json')
    def edit_object_categories_list(self):
        object_category_deserialized = self.schema.deserialize(self.request.json_body)
        object_category_deserialized['id'] = int(self.request.matchdict['id'])

        object_category = self.serializer.convert_schema_to_object(object_category_deserialized)
        self.service.update_object_category(object_category)
        return {'id': id}
