from pyramid.httpexceptions import HTTPNoContent, HTTPCreated
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import RealtyTypeSchema
from .serializer import RealtyTypeSerializer
from .service import RealtyTypeService


@view_defaults(renderer='json')
class RealtyTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.service = RealtyTypeService()
        self.serializer = RealtyTypeSerializer()
        self.schema = RealtyTypeSchema()

    @view_config(route_name='get_all_realty_types')
    def get_all_realty_types(self):
        realty_types = self.service.get_all_realty_types()
        return self.serializer.convert_list_to_json(realty_types)

    @view_config(route_name='add_realty_type')
    def add_realty_type(self):
        realty_type_deserialized = self.schema.deserialize(self.request.json_body)

        realty_type = self.serializer.to_mapped_object(realty_type_deserialized)
        self.service.add_realty_type(realty_type)
        return HTTPCreated(json_body={'id': realty_type.realty_types_id})

    @view_config(route_name='delete_realty_type')
    def delete_realty_type(self):
        id_ = self.get_id()
        self.service.delete_realty_type_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_realty_type')
    def edit_realty_type(self):
        realty_type_deserialized = self.schema.deserialize(self.request.json_body)
        realty_type_deserialized['id'] = self.get_id()

        new_realty_type = self.serializer.to_mapped_object(realty_type_deserialized)
        self.service.update_realty_type(new_realty_type)
        return {'id': self.get_id()}

    @view_config(route_name='get_realty_type')
    def get_realty_type(self):
        id_ = self.get_id()
        realty_type = self.service.get_realty_type_by_id(id_)
        return self.serializer.to_json(realty_type)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
