from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.work_list import WorkListSchema
from mks_backend.serializers.work_list import WorkListSerializer
from mks_backend.services.work_list import WorkListService

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class WorkListController:

    def __init__(self, request: Request):
        self.request = request
        self.service = WorkListService()
        self.serializer = WorkListSerializer()
        self.schema = WorkListSchema()

    @view_config(route_name='get_work_list_for_construction_object')
    def get_work_list_for_construction_object(self):
        construction_object_id = self.get_id()
        work_list = self.service.get_work_list_for_construction_object(construction_object_id)
        return self.serializer.convert_list_to_json(work_list)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_work_list')
    def add_work_list(self):
        work_list_deserialized = self.schema.deserialize(self.request.json_body)

        work_list = self.serializer.convert_schema_to_object(work_list_deserialized)
        self.service.add_work_list(work_list)
        return {'id': work_list.works_list_id}

    @view_config(route_name='delete_work_list')
    def delete_work_list(self):
        id = self.get_id()
        self.service.delete_work_list_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_work_list')
    def edit_work_list(self):
        work_list_deserialized = self.schema.deserialize(self.request.json_body)
        work_list_deserialized['id'] = self.get_id()

        new_work_list = self.serializer.convert_schema_to_object(work_list_deserialized)
        self.service.update_work_list(new_work_list)
        return {'id': self.get_id()}

    @view_config(route_name='get_work_list')
    def get_work_list(self):
        id = self.get_id()
        work_list = self.service.get_work_list_by_id(id)
        return self.serializer.convert_object_to_json(work_list)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
