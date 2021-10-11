from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ConstructionCriticalCategorySchema
from .serializer import ConstructionCriticalCategorySerializer
from .service import ConstructionCriticalCategoryService

@view_defaults(renderer='json')
class ConstructionCriticalCategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionCriticalCategorySerializer()
        self.service = ConstructionCriticalCategoryService()
        self.schema = ConstructionCriticalCategorySchema()

    @view_config(route_name='get_all_construction_critical_categories')
    def get_all_construction_critical_categories(self):
        construction_critical_categories = self.service.get_all_construction_categories()
        return self.serializer.convert_list_to_json(construction_critical_categories)

    @view_config(route_name='add_construction_critical_category')
    def add_construction_critical_category(self):
        construction_critical_categories_deserialized = self.schema.deserialize(self.request.json_body)

        construction_critical_category = self.serializer.convert_schema_to_object(construction_critical_categories_deserialized)
        self.service.add_construction_critical_category(construction_critical_category)

        return {'id': construction_critical_category.construction_critical_categories_id}

    @view_config(route_name='get_construction_critical_category')
    def get_construction_critical_category(self):
        id_ = int(self.request.matchdict['id'])
        construction_critical_category = self.service.get_construction_critical_category_by_id(id_)
        return self.serializer.convert_object_to_json(construction_critical_category)

    @view_config(route_name='delete_construction_critical_category')
    def delete_construction_critical_category(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_critical_category_by_id(id_)
        return {'id': id_}

    @view_config(route_name='edit_construction_critical_category')
    def edit_construction_critical_category(self):
        construction_critical_categories_deserialized = self.schema.deserialize(self.request.json_body)
        id_ = int(self.request.matchdict['id'])
        construction_critical_categories_deserialized['id'] = id_

        construction_critical_category = self.serializer.convert_schema_to_object(construction_critical_categories_deserialized)
        self.service.update_construction_critical_category(construction_critical_category)
        return {'id': id_}

