from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.serializers.constructions.subcategory_list import SubcategoryListSerializer
from mks_backend.services.constructions.subcategory_list import SubcategoryListService


@view_defaults(renderer='json')
class SubcategoryListController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = SubcategoryListSerializer()
        self.service = SubcategoryListService()

    @view_config(route_name='get_subcategories_lists')
    def get_all_subcategories_lists(self):
        subcategories_lists = self.service.get_all_subcategories_lists()
        return self.serializer.convert_list_to_json(subcategories_lists)
