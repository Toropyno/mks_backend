from pyramid.view import view_config

#from mks_backend.services.object_categories_service import ConstructionStagesService
#from mks_backend.serializers.object_categories_serializer import ConstructionStagesSerializer


class ObjectCategoriesController(object):

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


    @view_config(route_name='add_object_category', request_method='GET', renderer='json')
    def get_object_category(self):
        pass
        #id = self.request.matchdict['id']
        #object_category = self.service.get_object_category_by_id(id)
        #json = self.serializer.convert_object_to_json(object_category)
        #return json

    @view_config(route_name='add_object_category', request_method='POST', renderer='json')
    def add_object_category(self):
        pass
        # object_category= self.service.get_object(self.request.json_body)
        # object_category = self.service.add_object_category(object_categories_list)
        # return {'id': object_category.object_category_id}

    @view_config(route_name='object_category_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        pass
        # id = self.request.matchdict['id']
        # self.service.delete_object_category_by_id(id)
        # return {'id': id}

    @view_config(route_name='object_category_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_object_categories_list(self):
        pass
        # id = self.request.matchdict['id']
        # object_category = self.service.get_object(self.request.json_body)
        # object_category = self.service.update_object_category(object_categories_list)
        # return {'id': object_category.object_category_id}