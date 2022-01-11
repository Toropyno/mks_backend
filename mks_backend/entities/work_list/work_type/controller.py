from pyramid.httpexceptions import HTTPNoContent, HTTPCreated
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import WorkTypeSchema
from .serializer import WorkTypeSerializer
from .service import WorkTypeService


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

    @view_config(route_name='add_work_type')
    def add_work_type(self):
        work_type_deserialized = self.schema.deserialize(self.request.json_body)

        work_type = self.serializer.to_mapped_object(work_type_deserialized)
        self.service.add_work_type(work_type)
        return HTTPCreated(json_body={'id': work_type.work_types_id})

    @view_config(route_name='delete_work_type')
    def delete_work_type(self):
        id_ = self.get_id()
        self.service.delete_work_type_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_work_type')
    def edit_work_type(self):
        work_type_deserialized = self.schema.deserialize(self.request.json_body)
        work_type_deserialized['id'] = self.get_id()

        new_work_type = self.serializer.to_mapped_object(work_type_deserialized)
        self.service.update_work_type(new_work_type)
        return {'id': new_work_type.work_types_id}

    @view_config(route_name='get_work_type')
    def get_work_type(self):
        id_ = self.get_id()
        work_type = self.service.get_work_type_by_id(id_)
        return self.serializer.to_json(work_type)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
