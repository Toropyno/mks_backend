from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ConstructionTypeSchema
from .serializer import ConstructionTypeSerializer
from .service import ConstructionTypeService


@view_defaults(renderer='json')
class ConstructionTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionTypeService()
        self.serializer = ConstructionTypeSerializer()
        self.schema = ConstructionTypeSchema()

    @view_config(route_name='get_all_construction_types')
    def get_all_construction_types(self):
        construction_types = self.service.get_all_construction_types()
        return self.serializer.convert_list_to_json(construction_types)

    @view_config(route_name='add_construction_type')
    def add_construction_type(self):
        construction_type_deserialized = self.schema.deserialize(self.request.json_body)

        construction_type = self.serializer.to_mapped_object(construction_type_deserialized)
        self.service.add_construction_type(construction_type)
        return {'id': construction_type.construction_types_id}

    @view_config(route_name='delete_construction_type')
    def delete_construction_type(self):
        id_ = self.get_id()
        self.service.delete_construction_type_by_id(id_)
        return {'id': id_}

    @view_config(route_name='edit_construction_type')
    def edit_construction_type(self):
        construction_type_deserialized = self.schema.deserialize(self.request.json_body)
        construction_type_deserialized['id'] = self.get_id()

        new_construction_type = self.serializer.to_mapped_object(construction_type_deserialized)
        self.service.update_construction_type(new_construction_type)
        return {'id': new_construction_type.construction_types_id}

    @view_config(route_name='get_construction_type')
    def get_construction_type(self):
        id_ = self.get_id()
        construction_type = self.service.get_construction_type_by_id(id_)
        return self.serializer.to_json(construction_type)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
