from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ConstructionSubcategorySchema
from .serializer import ConstructionSubcategorySerializer
from .service import ConstructionSubcategoryService


@view_defaults(renderer='json')
class ConstructionSubcategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionSubcategorySerializer()
        self.service = ConstructionSubcategoryService()
        self.schema = ConstructionSubcategorySchema()

    @view_config(route_name='get_all_construction_subcategories')
    def get_all_construction_subcategories(self):
        construction_subcategories = self.service.get_all_construction_subcategories()
        return self.serializer.convert_list_to_json(construction_subcategories)

    @view_config(route_name='add_construction_subcategory')
    def add_construction_subcategory(self):
        construction_subcategories_deserialized = self.schema.deserialize(self.request.json_body)
        construction_subcategory = self.serializer.convert_schema_to_object(construction_subcategories_deserialized)

        self.service.add_construction_subcategory(construction_subcategory)
        return {'id': construction_subcategory.construction_subcategories_id}

    @view_config(route_name='get_construction_subcategory')
    def get_construction_subcategory(self):
        id_ = int(self.request.matchdict['id'])
        construction_subcategory = self.service.get_construction_subcategory_by_id(id_)
        return self.serializer.to_json(construction_subcategory)

    @view_config(route_name='delete_construction_subcategory')
    def delete_construction_subcategory(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_subcategory_by_id(id_)
        return {'id': id_}

    @view_config(route_name='edit_construction_subcategory')
    def edit_construction_subcategory(self):
        construction_subcategories_deserialized = self.schema.deserialize(self.request.json_body)
        id_ = int(self.request.matchdict['id'])
        construction_subcategories_deserialized['id'] = id_

        construction_subcategory = self.serializer.convert_schema_to_object(construction_subcategories_deserialized)
        self.service.update_construction_subcategory(construction_subcategory)
        return {'id': id_}
