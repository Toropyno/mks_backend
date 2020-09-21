from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.serializers.object_category_list import ObjectCategoryListSerializer
from mks_backend.services.object_category_list import ObjectCategoryListService


class ObjectCategoryListController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ObjectCategoryListService()
        self.serializer = ObjectCategoryListSerializer()

    @view_config(route_name='get_object_categories_lists', renderer='json')
    def get_all_object_categories_lists(self):
        object_categories_lists = self.service.get_all_object_categories_lists()
        return self.serializer.convert_list_to_json(object_categories_lists)