from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ConstructionCategorySchema
from .serializer import ConstructionCategorySerializer
from .service import ConstructionCategoryService


@view_defaults(renderer='json')
class ConstructionCategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionCategorySerializer()
        self.service = ConstructionCategoryService()
        self.schema = ConstructionCategorySchema()

    @view_config(route_name='get_all_construction_categories')
    def get_all_construction_categories(self):
        construction_categories = self.service.get_all_construction_categories()
        return self.serializer.convert_list_to_json(construction_categories)

    @view_config(route_name='add_construction_category')
    def add_construction_category(self):
        construction_categories_deserialized = self.schema.deserialize(self.request.json_body)

        construction_category = self.service.to_mapped_object(construction_categories_deserialized)
        self.service.add_construction_category(construction_category)

        return HTTPCreated(json_body={'id': construction_category.construction_categories_id})

    @view_config(route_name='get_construction_category')
    def get_construction_category(self):
        id_ = int(self.request.matchdict['id'])
        construction_category = self.service.get_construction_category_by_id(id_)
        return self.serializer.to_json(construction_category)

    @view_config(route_name='delete_construction_category')
    def delete_construction_category(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_category_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_construction_category')
    def edit_construction_category(self):
        construction_categories_deserialized = self.schema.deserialize(self.request.json_body)
        id_ = int(self.request.matchdict['id'])
        construction_categories_deserialized['id'] = id_

        construction_category = self.service.to_mapped_object(construction_categories_deserialized)
        self.service.update_construction_category(construction_category)
        return {'id': id_}
