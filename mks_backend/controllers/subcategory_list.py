import colander
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from mks_backend.controllers.schemas.subcategory_list import SubcategoryListSchema
from mks_backend.errors.colander_error import get_collander_error_dict
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.subcategory_list import SubcategoryListSerializer
from mks_backend.services.subcategory_list import SubcategoryListService


class SubcategoryListController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = SubcategoryListSerializer()
        self.service = SubcategoryListService()
        self.schema = SubcategoryListSchema()

    @view_config(route_name='subcategories_lists', request_method='GET', renderer='json')
    def get_all_subcategories_lists(self):
        subcategories_lists = self.service.get_all_subcategories_lists()
        return self.serializer.convert_list_to_json(subcategories_lists)

    @view_config(route_name='add_subcategories_list', request_method='POST', renderer='json')
    def add_subcategories_list(self):
        try:
            subcategories_list_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

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
