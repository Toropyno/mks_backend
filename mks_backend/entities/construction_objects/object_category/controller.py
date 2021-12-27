from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ObjectCategorySchema
from .serializer import ObjectCategorySerializer
from .service import ObjectCategoryService


@view_defaults(renderer='json')
class ObjectCategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ObjectCategoryService()
        self.serializer = ObjectCategorySerializer()
        self.schema = ObjectCategorySchema()

    @view_config(route_name='get_all_object_categories')
    def get_all_object_categories(self):
        object_categories = self.service.get_all_object_categories()
        return self.serializer.convert_list_to_json(object_categories)

    @view_config(route_name='get_object_category')
    def get_object_category(self):
        id = int(self.request.matchdict['id'])
        object_category = self.service.get_object_category_by_id(id)
        return self.serializer.to_json(object_category)

    @view_config(route_name='add_object_category')
    def add_object_category(self):
        object_category_deserialized = self.schema.deserialize(self.request.json_body)
        object_category = self.serializer.to_mapped_object(object_category_deserialized)

        self.service.add_object_category(object_category)
        return {'id': object_category.object_categories_id}

    @view_config(route_name='delete_object_category')
    def delete_construction_object(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_object_category_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_object_category', request_method='PUT')
    def edit_object_categories_list(self):
        object_category_deserialized = self.schema.deserialize(self.request.json_body)
        object_category_deserialized['id'] = int(self.request.matchdict['id'])

        object_category = self.serializer.to_mapped_object(object_category_deserialized)
        self.service.update_object_category(object_category)
        return {'id': object_category.object_categories_id}
