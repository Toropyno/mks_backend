import colander
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from mks_backend.controllers.schemas.object_category import ObjectCategorySchema
from mks_backend.errors.colander_error import get_collander_error_dict
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.object_category import ObjectCategorySerializer
from mks_backend.services.object_category import ObjectCategoryService


class ObjectCategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ObjectCategoryService()
        self.serializer = ObjectCategorySerializer()
        self.schema = ObjectCategorySchema()

    @view_config(route_name='get_all_object_categories', renderer='json')
    def get_all_object_categories(self):
        object_categories = self.service.get_all_object_categories()
        return self.serializer.convert_list_to_json(object_categories)

    @view_config(route_name='get_object_category', renderer='json')
    def get_object_category(self):
        id = int(self.request.matchdict['id'])
        object_category = self.service.get_object_category_by_id(id)
        return self.serializer.convert_object_to_json(object_category)

    @view_config(route_name='add_object_category', renderer='json')
    def add_object_category(self):
        try:
            object_category_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))
        object_category = self.serializer.convert_schema_to_object(object_category_deserialized)
        try:
            self.service.add_object_category(object_category)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': object_category.object_categories_id}

    @view_config(route_name='delete_object_category', renderer='json')
    def delete_construction_object(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_object_category_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_object_category', request_method='PUT', renderer='json')
    def edit_object_categories_list(self):
        id = int(self.request.matchdict['id'])
        try:
            object_category_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))
        object_category_deserialized['id'] = id
        object_category = self.serializer.convert_schema_to_object(object_category_deserialized)
        try:
            self.service.update_object_category(object_category)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': id}