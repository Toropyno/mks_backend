from pyramid.view import view_config

from mks_backend.serializers.construction_subcategories_serializer import ConstructionSubcategoriesSerializer
from mks_backend.services.construction_subcategories_service import ConstructionSubcategoriesService


class ConstructionSubcategoryController(object):

    def __init__(self, request):
        self.request = request
        self.serializer = ConstructionSubcategoriesSerializer()
        self.service = ConstructionSubcategoriesService()

    @view_config(route_name='construction_subcategories', request_method='GET', renderer='json')
    def get_all_construction_subcategories(self):
        construction_subcategories_array = self.service.get_all_construction_subcategories()
        json = self.serializer.convert_list_to_json(construction_subcategories_array)
        return json

    @view_config(route_name='add_construction_subcategory', request_method='POST', renderer='json')
    def add_construction_subcategory(self):
        construction_subcategory = self.service.get_object(self.request.json_body)
        self.service.add_construction_subcategory(construction_subcategory)
        return {'id': construction_subcategory.construction_subcategories_id}

    @view_config(route_name='construction_subcategory_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_subcategory(self):
        id = self.request.matchdict['id']
        construction_subcategory = self.service.get_construction_subcategory_by_id(id)
        json = self.serializer.convert_object_to_json(construction_subcategory)
        return json

    @view_config(route_name='construction_subcategory_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_subcategory(self):
        id = self.request.matchdict['id']
        self.service.delete_construction_subcategory_by_id(id)
        return {'id': id}

    @view_config(route_name='construction_subcategory_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_subcategory(self):
        id = self.request.matchdict['id']
        new_construction_subcategory = self.service.get_object(self.request.json_body)
        new_construction_subcategory.construction_subcategory_id = id
        self.service.update_construction_subcategory(new_construction_subcategory)
        return {'id': new_construction_subcategory.construction_subcategories_id}