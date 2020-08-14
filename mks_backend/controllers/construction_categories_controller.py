from pyramid.view import view_config


# from mks_backend.serializers.construction_category_serializer import ConstructionCategorySerializer
from mks_backend.services.construction_categories_service import ConstructionCategoriesService


class ConstructionCategoryController(object):

    def __init__(self, request):
        self.request = request
        # self.serializer = ConstructionCategoriesSerializer()
        self.service = ConstructionCategoriesService()

    @view_config(route_name='construction_categories', request_method='GET', renderer='json')
    def get_all_construction_categories(self):
        construction_categories_array = self.service.get_all_construction_categories()
        json = [] #self.serializer.convert_list_to_json(construction_categories_array)
        return json

    @view_config(route_name='add_construction_category', request_method='POST', renderer='json')
    def add_construction_category(self):
        construction_category = self.service.get_object(self.request.json_body)
        self.service.add_construction_category(construction_category)
        return {'id': construction_category.construction_category_id}

    @view_config(route_name='construction_category_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_category(self):
        id = self.request.matchdict['id']
        construction_category = self.service.get_construction_category_by_id(id)
        json = [] # self.serializer.convert_object_to_json(construction_category)
        return json

    @view_config(route_name='construction_category_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_category(self):
        id = self.request.matchdict['id']
        self.service.delete_construction_category_by_id(id)
        return {'id': id}
        pass

    @view_config(route_name='construction_category_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_category(self):
        id = self.request.matchdict['id']
        new_construction_category = self.service.get_object(self.request.json_body)
        new_construction_category.construction_category_id = id
        new_construction_category = self.service.update_construction_category(new_construction_category)
        return {'id': new_construction_category.construction_categories_id}