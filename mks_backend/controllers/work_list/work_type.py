from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.work_list.work_type import WorkTypeSchema
from mks_backend.serializers.work_list.work_type import WorkTypeSerializer
from mks_backend.services.work_list.work_type import WorkTypeService

from mks_backend.errors import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class WorkTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.service = WorkTypeService()
        self.serializer = WorkTypeSerializer()
        self.schema = WorkTypeSchema()

    @view_config(route_name='get_all_work_types')
    def get_all_work_types(self):
        work_types = self.service.get_all_work_types()
        return self.serializer.convert_list_to_json(work_types)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_work_type')
    def add_work_type(self):
        work_type_deserialized = self.schema.deserialize(self.request.json_body)

        work_type = self.serializer.convert_schema_to_object(work_type_deserialized)
        self.service.add_work_type(work_type)
        return {'id': work_type.work_types_id}

    @view_config(route_name='delete_work_type')
    def delete_work_type(self):
        id = self.get_id()
        self.service.delete_work_type_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_work_type')
    def edit_work_type(self):
        work_type_deserialized = self.schema.deserialize(self.request.json_body)
        work_type_deserialized['id'] = self.get_id()

        new_work_type = self.serializer.convert_schema_to_object(work_type_deserialized)
        self.service.update_work_type(new_work_type)
        return {'id': new_work_type.work_types_id}

    @view_config(route_name='get_work_type')
    def get_work_type(self):
        id = self.get_id()
        work_type = self.service.get_work_type_by_id(id)
        return self.serializer.convert_object_to_json(work_type)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
