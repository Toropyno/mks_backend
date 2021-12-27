from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import CriticalCategorySchema
from .serializer import CriticalCategorySerializer
from .service import CriticalCategoryService


@view_defaults(renderer='json')
class CriticalCategoryController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = CriticalCategorySerializer()
        self.service = CriticalCategoryService()
        self.schema = CriticalCategorySchema()

    @view_config(route_name='get_all_critical_categories')
    def get_all_critical_categories(self):
        critical_categories = self.service.get_all_construction_categories()
        return self.serializer.list_to_json(critical_categories)

    @view_config(route_name='add_critical_category')
    def add_critical_category(self):
        critical_category_deserialized = self.schema.deserialize(self.request.json_body)

        critical_category = self.serializer.to_mapped_object(
            critical_category_deserialized
        )
        self.service.add_critical_category(critical_category)

        return {'id': critical_category.critical_categories_id}

    @view_config(route_name='get_critical_category')
    def get_critical_category(self):
        id_ = int(self.request.matchdict['id'])
        critical_category = self.service.get_critical_category_by_id(id_)
        return self.serializer.to_json(critical_category)

    @view_config(route_name='delete_critical_category')
    def delete_critical_category(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_critical_category_by_id(id_)
        return {'id': id_}

    @view_config(route_name='edit_critical_category')
    def edit_critical_category(self):
        critical_category_deserialized = self.schema.deserialize(self.request.json_body)
        id_ = int(self.request.matchdict['id'])
        critical_category_deserialized['id'] = id_

        critical_category = self.serializer.to_mapped_object(
            critical_category_deserialized
        )
        self.service.update_critical_category(critical_category)
        return {'id': id_}
