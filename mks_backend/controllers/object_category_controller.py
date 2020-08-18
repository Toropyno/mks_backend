import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.services.object_category_service import ObjectCategoryService
from mks_backend.serializers.object_category_serializer import ObjectCategorySerializer
from mks_backend.controllers.schemas.object_categories_schema import ObjectCategoriesSchema


class ObjectCategoryController(object):

    def __init__(self, request):
        self.request = request
        self.service = ObjectCategoryService()
        self.serializer = ObjectCategorySerializer()

    @view_config(route_name='object_categories', request_method='GET', renderer='json')
    def get_all_object_categories(self):
        object_categories = self.service.get_all_object_categories()
        json = self.serializer.convert_list_to_json(object_categories)
        return json

    @view_config(route_name='add_object_category', request_method='GET', renderer='json')
    def get_object_category(self):
        id = self.request.matchdict['id']
        object_category = self.service.get_object_category_by_id(id)
        json = self.serializer.convert_object_to_json(object_category)
        return json

    @view_config(route_name='add_object_category', request_method='POST', renderer='json')
    def add_object_category(self):
        object_category_schema = ObjectCategoriesSchema()
        try:
            object_category_deserialized = object_category_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        object_category = self.serializer.convert_schema_to_object(object_category_deserialized)
        object_category = self.service.add_object_category(object_category)
        return {'id': object_category.object_category_id}

    @view_config(route_name='object_category_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        id = self.request.matchdict['id']
        self.service.delete_object_category_by_id(id)
        return {'id': id}

    @view_config(route_name='object_category_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_object_categories_list(self):
        id = self.request.matchdict['id']
        object_category_schema = ObjectCategoriesSchema()
        try:
            object_category_deserialized = object_category_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        object_category_deserialized['id'] = id
        object_category = self.serializer.convert_schema_to_object(object_category_deserialized)
        self.service.update_object_category(object_category)
        return {'id': id}
