import colander
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request

from mks_backend.controllers.schemas.subcategories_list_schema import SubcategoriesListSchema
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.subcategories_list_serializer import SubcategoriesListSerializer
from mks_backend.services.subcategories_list_service import SubcategoriesListService


class SubcategoriesListController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = SubcategoriesListSerializer()
        self.service = SubcategoriesListService()
        self.schema = SubcategoriesListSchema()

    @view_config(route_name='subcategories_lists', request_method='GET', renderer='json')
    def get_all_subcategories_lists(self):
        subcategories_lists = self.service.get_all_subcategories_lists()
        return self.serializer.convert_list_to_json(subcategories_lists)

    @view_config(route_name='add_subcategories_list', request_method='POST', renderer='json')
    def add_subcategories_list(self):
        try:
            subcategories_list_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())

        subcategories_list = self.serializer.convert_schema_to_object(subcategories_list_deserialized)
        try:
            self.service.add_subcategories_list(subcategories_list)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': subcategories_list.subcategories_list_id}

    @view_config(route_name='subcategories_list_delete_and_view', request_method='GET', renderer='json')
    def get_subcategories_list(self):
        id = int(self.request.matchdict['id'])
        subcategories_list = self.service.get_subcategories_list_by_id(id)
        return self.serializer.convert_object_to_json(subcategories_list)

    @view_config(route_name='subcategories_list_delete_and_view', request_method='DELETE', renderer='json')
    def delete_subcategories_list(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_subcategories_list_by_id(id)
        return {'id': id}
