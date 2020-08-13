from pyramid.view import view_config

#from mks_backend.services.object_categories_service import ConstructionStagesService
#from mks_backend.serializers.object_categories_serializer import ConstructionStagesSerializer



class ConstructionStagesController(object):

    def __init__(self, request):
        self.request = request
        self.service = None #ObjectCategoriesService()
        self.serializer = None #ObjectCategoriesSerializer()

    @view_config(route_name='object_categories', request_method='GET', renderer='json')
    def get_all_object_categories(self):
        pass
        #object_categories_array = self.service.get_all_object_categories_list()
        #json = self.serializer.convert_list_to_json(object_categories_array)
        #return json


    @view_config(route_name='object_category_view', request_method='GET', renderer='json')
    def get_object_category(self):
        pass
        #id = self.request.matchdict['id']
        #object_category = self.service.get_object_category_by_id(id)
        #json = self.serializer.convert_object_to_json(object_category)
        #return json