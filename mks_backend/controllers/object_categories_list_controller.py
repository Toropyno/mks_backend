import colander
from pyramid.view import view_config
from pyramid.response import Response

#from mks_backend.services.object_categories_list_service import ObjectCategoriesListService
#from mks_backend.serializers.object_categories_list_serializer import ObjectCategoriesListSerializer



class ConstructionStagesController(object):

    def __init__(self, request):
        self.request = request
        self.service = None #ObjectCategoriesListService()
        self.serializer = None #ObjectCategoriesListSerializer()

    @view_config(route_name='object_categories_lists', request_method='GET', renderer='json')
    def get_all_object_categories_lists(self):
        pass
        #object_categories_lists_array = self.service.get_all_object_categories_lists()
        #json = self.serializer.convert_list_to_json(object_categories_lists_array)
        #return json

    @view_config(route_name='add_object_categories_list', request_method='POST', renderer='json')
    def add_object_categories_list(self):
        pass
        #object_categories_list = self.service.get_object(self.request.json_body)
        #object_categories_list = self.service.add_object_categories_list(object_categories_list)
        #return {'id': object_categories_list.object_categories_list_id}

    @view_config(route_name='object_categories_lists_delete_change_and_view', request_method='GET', renderer='json')
    def get_object_categories_list(self):
        pass
        #id = self.request.matchdict['id']
        #object_categories_list = self.service.get_object_categories_list_by_id(id)
        #json = self.serializer.convert_object_to_json(object_categories_list)
        #return json

    @view_config(route_name='object_categories_lists_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        pass
        #id = self.request.matchdict['id']
        #self.service.delete_object_categories_list_by_id(id)
        #return {'id': id}

    @view_config(route_name='object_categories_lists_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_object_categories_list(self):
        pass
        #id = self.request.matchdict['id']
        #object_categories_list = self.service.get_object(self.request.json_body)
        #object_categories_list = self.service.update_object_categories_list(object_categories_list)
        #return {'id': object_categories_list.object_categories_list}