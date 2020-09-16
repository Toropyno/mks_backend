import colander
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.controllers.schemas.construction_category import ConstructionCategorySchema
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.construction_category import ConstructionCategorySerializer
from mks_backend.services.construction_category import ConstructionCategoryService
from mks_backend.errors.colander_error import get_collander_error_dict


class ConstructionCategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionCategorySerializer()
        self.service = ConstructionCategoryService()
        self.schema = ConstructionCategorySchema()

    @view_config(route_name='get_construction_categories', renderer='json')
    def get_all_construction_categories(self):
        construction_categories = self.service.get_all_construction_categories()
        return self.serializer.convert_list_to_json(construction_categories)

    @view_config(route_name='add_construction_category', renderer='json')
    def add_construction_category(self):
        try:
            construction_categories_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        construction_category = self.service.convert_schema_to_object(construction_categories_deserialized)
        try:
            self.service.add_construction_category(construction_category)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': construction_category.construction_categories_id}

    @view_config(route_name='get_construction_category', renderer='json')
    def get_construction_category(self):
        id = int(self.request.matchdict['id'])
        construction_category = self.service.get_construction_category_by_id(id)
        return self.serializer.convert_object_to_json(construction_category)

    @view_config(route_name='delete_construction_category', renderer='json')
    def delete_construction_category(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_category_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_construction_category', renderer='json')
    def edit_construction_category(self):
        id = int(self.request.matchdict['id'])
        try:
            construction_categories_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        construction_categories_deserialized['id'] = id
        construction_category = self.service.convert_schema_to_object(construction_categories_deserialized)
        try:
            self.service.update_construction_category(construction_category)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': id}
