import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.services.object_categories_list_service import ObjectCategoriesListService
from mks_backend.serializers.object_categories_list_serializer import ObjectCategoriesListSerializer
from mks_backend.controllers.schemas.object_categories_list_schema import ObjectCategoriesListSchema


class ObjectCategoriesListController(object):

    def __init__(self, request):
        self.request = request
        self.service = ObjectCategoriesListService()
        self.serializer = ObjectCategoriesListSerializer()
        self.schema = ObjectCategoriesListSchema()

    @view_config(route_name='object_categories_lists', request_method='GET', renderer='json')
    def get_all_object_categories_lists(self):
        object_categories_lists = self.service.get_all_object_categories_lists()
        json = self.serializer.convert_list_to_json(object_categories_lists)
        return json

    @view_config(route_name='add_object_categories_list', request_method='POST', renderer='json')
    def add_object_categories_list(self):
        try:
            object_categories_list_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        object_categories_list = self.serializer.convert_schema_to_object(object_categories_list_deserialized)
        try:
            self.service.add_object_categories_list(object_categories_list)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})
        return {'id': object_categories_list.object_categories_list_id}

    @view_config(route_name='object_categories_list_delete_change_and_view', request_method='GET', renderer='json')
    def get_object_categories_list(self):
        id = self.request.matchdict['id']
        object_categories_list = self.service.get_object_categories_list_by_id(id)
        json = self.serializer.convert_object_to_json(object_categories_list)
        return json

    @view_config(route_name='object_categories_list_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        id = self.request.matchdict['id']
        self.service.delete_object_categories_list_by_id(id)
        return {'id': id}

    @view_config(route_name='object_categories_list_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_object_categories_list(self):
        id = self.request.matchdict['id']
        try:
            object_categories_list_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        object_categories_list_deserialized['id'] = id
        object_categories_list = self.serializer.convert_schema_to_object(object_categories_list_deserialized)
        self.service.update_object_categories_list(object_categories_list)
        return {'id': id}
