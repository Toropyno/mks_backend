import colander
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request

from mks_backend.services.object_category_list import ObjectCategoryListService
from mks_backend.serializers.object_category_list import ObjectCategoryListSerializer
from mks_backend.controllers.schemas.object_category_list import ObjectCategoryListSchema
from mks_backend.errors.db_basic_error import DBBasicError


class ObjectCategoryListController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ObjectCategoryListService()
        self.serializer = ObjectCategoryListSerializer()
        self.schema = ObjectCategoryListSchema()

    @view_config(route_name='object_categories_lists', request_method='GET', renderer='json')
    def get_all_object_categories_lists(self):
        object_categories_lists = self.service.get_all_object_categories_lists()
        return self.serializer.convert_list_to_json(object_categories_lists)

    @view_config(route_name='add_object_categories_list', request_method='POST', renderer='json')
    def add_object_categories_list(self):
        try:
            object_categories_list_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        object_categories_list = self.serializer.convert_schema_to_object(object_categories_list_deserialized)
        try:
            self.service.add_object_categories_list(object_categories_list)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': object_categories_list.object_categories_list_id}

    @view_config(route_name='object_categories_list_delete_change_and_view', request_method='GET', renderer='json')
    def get_object_categories_list(self):
        id = int(self.request.matchdict['id'])
        object_categories_list = self.service.get_object_categories_list_by_id(id)
        return self.serializer.convert_object_to_json(object_categories_list)

    @view_config(route_name='object_categories_list_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_object_categories_list_by_id(id)
        return {'id': id}

    @view_config(route_name='object_categories_list_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_object_categories_list(self):
        id = int(self.request.matchdict['id'])
        try:
            object_categories_list_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        object_categories_list_deserialized['id'] = id
        object_categories_list = self.serializer.convert_schema_to_object(object_categories_list_deserialized)
        try:
            self.service.update_object_categories_list(object_categories_list)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': id}
