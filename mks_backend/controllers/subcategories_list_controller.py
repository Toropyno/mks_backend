from pyramid.view import view_config

# from mks_backend.serializers.subcategories_list_serializer import SubcategoriesListSerializer
# from mks_backend.services.subcategories_list_service import SubcategoriesListService


class SubcategoriesListController(object):

    def __init__(self, request):
        self.request = request
        # self.serializer = SubcategoriesListSerializer()
        # self.service = SubcategoriesListService()

    @view_config(route_name='subcategories_lists', request_method='GET', renderer='json')
    def get_all_subcategories_lists(self):
        # if self.request.params:
        #     subcategories_lists_array = self.service.filter_subcategories_list(self.request.params)
        # else:
        #     subcategories_lists_array = self.service.get_all_subcategories_lists()
        #
        # json = self.serializer.convert_list_to_json(subcategories_lists_array)
        # return json
        pass

    @view_config(route_name='add_subcategories_list', request_method='POST', renderer='json')
    def add_subcategories_list(self):
        pass
