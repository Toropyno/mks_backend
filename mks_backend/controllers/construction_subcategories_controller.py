import colander
from pyramid.response import Response
from pyramid.view import view_config

from mks_backend.controllers.schemas.construction_subcategories_schema import ConstructionSubcategoriesSchema
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.construction_subcategory_serializer import ConstructionSubcategoriesSerializer
from mks_backend.services.construction_subcategory_service import ConstructionSubcategoriesService


class ConstructionSubcategoryController:

    def __init__(self, request):
        self.request = request
        self.serializer = ConstructionSubcategoriesSerializer()
        self.service = ConstructionSubcategoriesService()
        self.schema = ConstructionSubcategoriesSchema()

    @view_config(route_name='construction_subcategories', request_method='GET', renderer='json')
    def get_all_construction_subcategories(self):
        construction_subcategories = self.service.get_all_construction_subcategories()
        json = self.serializer.convert_list_to_json(construction_subcategories)
        return json

    @view_config(route_name='add_construction_subcategory', request_method='POST', renderer='json')
    def add_construction_subcategory(self):
        try:
            construction_subcategories_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())

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
        json = self.serializer.convert_object_to_json(construction_subcategory)
        return json

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
            return Response(status=403, json_body=error.asdict())

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
