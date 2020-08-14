from pyramid.view import view_config


# from mks_backend.serializers.subcategories_list_serializer import SubcategoriesListSerializer
from mks_backend.services.subcategories_list_service import SubcategoriesListService


class SubcategoriesListController(object):

    def __init__(self, request):
        self.request = request
        # self.serializer = SubcategoriesListSerializer()
        self.service = SubcategoriesListService()

    @view_config(route_name='subcategories_lists', request_method='GET', renderer='json')
    def get_all_subcategories_lists(self):
        subcategories_lists_array = self.service.get_all_subcategories_lists()
        json = [] # self.serializer.convert_list_to_json(subcategories_lists_array)
        return json

    @view_config(route_name='add_subcategories_list', request_method='POST', renderer='json')
    def add_subcategories_list(self):
        subcategories_list = self.service.get_object(self.request.json_body)
        self.service.add_subcategories_list(subcategories_list)
        return {'id': subcategories_list.subcategories_list_id}

    @view_config(route_name='subcategories_list_delete_and_view', request_method='GET', renderer='json')
    def get_subcategories_list(self):
        id = self.request.matchdict['id']
        subcategories_list = self.service.get_subcategories_list_by_id(id)
        json = [] # self.serializer.convert_object_to_json(subcategories_list)
        return json

    @view_config(route_name='subcategories_list_delete_and_view', request_method='DELETE', renderer='json')
    def delete_subcategories_list(self):
        id = self.request.matchdict['id']
        self.service.delete_subcategories_list_by_id(id)
        return {'id': id}