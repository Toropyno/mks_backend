from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ElementTypeSchema
from .serializer import ElementTypeSerializer
from .service import ElementTypeService


@view_defaults(renderer='json')
class ElementTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ElementTypeSerializer()
        self.service = ElementTypeService()
        self.schema = ElementTypeSchema()

    @view_config(route_name='get_all_element_types')
    def get_all_element_types(self):
        element_types = self.service.get_all_element_types()
        return self.serializer.convert_list_to_json(element_types)

    @view_config(route_name='add_element_type')
    def add_element_type(self):
        element_type_deserialized = self.schema.deserialize(self.request.json_body)
        element_type = self.serializer.convert_schema_to_object(element_type_deserialized)
        self.service.add_element_type(element_type)
        return {'id': element_type.element_types_id}

    @view_config(route_name='get_element_type')
    def get_element_type(self):
        id = int(self.request.matchdict['id'])
        element_type = self.service.get_element_type_by_id(id)
        return self.serializer.convert_object_to_json(element_type)

    @view_config(route_name='delete_element_type')
    def delete_element_type(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_element_type_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_element_type')
    def edit_element_type(self):
        id = int(self.request.matchdict['id'])
        element_type_deserialized = self.schema.deserialize(self.request.json_body)

        element_type_deserialized['id'] = id
        element_type = self.serializer.convert_schema_to_object(element_type_deserialized)

        self.service.update_element_type(element_type)
        return {'id': id}