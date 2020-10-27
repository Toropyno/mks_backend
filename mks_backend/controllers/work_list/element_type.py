from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.controllers.schemas.work_list.element_type import ElementTypeSchema
from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
from mks_backend.serializers.work_list.element_type import ElementTypeSerializer
from mks_backend.services.work_list.element_type import ElementTypeService


class ElementTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ElementTypeSerializer()
        self.service = ElementTypeService()
        self.schema = ElementTypeSchema()

    @view_config(route_name='get_all_element_types', renderer='json')
    def get_all_element_types(self):
        element_types = self.service.get_all_element_types()
        return self.serializer.convert_list_to_json(element_types)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_element_type', renderer='json')
    def add_element_type(self):
        element_type_deserialized = self.schema.deserialize(self.request.json_body)
        element_type = self.serializer.convert_schema_to_object(element_type_deserialized)
        self.service.add_element_type(element_type)
        return {'id': element_type.element_types_id}

    @view_config(route_name='get_element_type', renderer='json')
    def get_element_type(self):
        id = int(self.request.matchdict['id'])
        element_type = self.service.get_element_type_by_id(id)
        return self.serializer.convert_object_to_json(element_type)

    @view_config(route_name='delete_element_type', renderer='json')
    def delete_element_type(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_element_type_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_element_type', renderer='json')
    def edit_element_type(self):
        id = int(self.request.matchdict['id'])
        element_type_deserialized = self.schema.deserialize(self.request.json_body)

        element_type_deserialized['id'] = id
        element_type = self.serializer.convert_schema_to_object(element_type_deserialized)

        self.service.update_element_type(element_type)
        return {'id': id}
