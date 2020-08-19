import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.controllers.schemas.construction_categories_schema import ConstructionCategoriesSchema
from mks_backend.serializers.construction_category_serializer import ConstructionCategoriesSerializer
from mks_backend.services.construction_category_service import ConstructionCategoriesService


class ConstructionCategoryController(object):

    def __init__(self, request):
        self.request = request
        self.serializer = ConstructionCategoriesSerializer()
        self.service = ConstructionCategoriesService()
        self.schema = ConstructionCategoriesSchema()

    @view_config(route_name='construction_categories', request_method='GET', renderer='json')
    def get_all_construction_categories(self):
        construction_categories = self.service.get_all_construction_categories()
        json = self.serializer.convert_list_to_json(construction_categories)
        return json

    @view_config(route_name='add_construction_category', request_method='POST', renderer='json')
    def add_construction_category(self):
        try:
            construction_categories_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())

        construction_category = self.serializer.convert_schema_to_object(construction_categories_deserialized)
        try:
            self.service.add_construction_category(construction_category)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})

        return {'id': construction_category.construction_categories_id}

    @view_config(route_name='construction_category_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_category(self):
        id = self.request.matchdict['id']
        construction_category = self.service.get_construction_category_by_id(id)
        json = self.serializer.convert_object_to_json(construction_category)
        return json

    @view_config(route_name='construction_category_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_category(self):
        id = self.request.matchdict['id']
        self.service.delete_construction_category_by_id(id)
        return {'id': id}
        pass

    @view_config(route_name='construction_category_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_category(self):
        id = self.request.matchdict['id']
        try:
            construction_categories_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())

        construction_categories_deserialized['id'] = id
        construction_category = self.serializer.convert_schema_to_object(construction_categories_deserialized)
        try:
            self.service.update_construction_category(construction_category)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})

        return {'id': id}
