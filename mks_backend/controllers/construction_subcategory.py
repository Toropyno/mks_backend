import colander
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request

from mks_backend.controllers.schemas.construction_subcategory import ConstructionSubcategorySchema
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.construction_subcategory import ConstructionSubcategorySerializer
from mks_backend.services.construction_subcategory import ConstructionSubcategoryService
from mks_backend.errors.colavder_error import get_dictionary_with_errors_correct_format


class ConstructionSubcategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionSubcategorySerializer()
        self.service = ConstructionSubcategoryService()
        self.schema = ConstructionSubcategorySchema()

    @view_config(route_name='construction_subcategories', request_method='GET', renderer='json')
    def get_all_construction_subcategories(self):
        construction_subcategories = self.service.get_all_construction_subcategories()
        return self.serializer.convert_list_to_json(construction_subcategories)

    @view_config(route_name='add_construction_subcategory', request_method='POST', renderer='json')
    def add_construction_subcategory(self):
        try:
            construction_subcategories_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_dictionary_with_errors_correct_format(error.asdict()))

        construction_subcategory = self.serializer.convert_schema_to_object(construction_subcategories_deserialized)
        try:
            self.service.add_construction_subcategory(construction_subcategory)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': construction_subcategory.construction_subcategories_id}

    @view_config(route_name='construction_subcategory_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_subcategory(self):
        id = int(self.request.matchdict['id'])
        construction_subcategory = self.service.get_construction_subcategory_by_id(id)
        return self.serializer.convert_object_to_json(construction_subcategory)

    @view_config(route_name='construction_subcategory_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_subcategory(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_subcategory_by_id(id)
        return {'id': id}

    @view_config(route_name='construction_subcategory_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_subcategory(self):
        id = int(self.request.matchdict['id'])
        try:
            construction_subcategories_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_dictionary_with_errors_correct_format(error.asdict()))

        construction_subcategories_deserialized['id'] = id
        construction_subcategory = self.serializer.convert_schema_to_object(construction_subcategories_deserialized)
        try:
            self.service.update_construction_subcategory(construction_subcategory)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': id}
