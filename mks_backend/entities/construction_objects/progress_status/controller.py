from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ProgressStatusSchema
from .serializer import ProgressStatusSerializer
from .service import ProgressStatusService


@view_defaults(renderer='json')
class ProgressStatusController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ProgressStatusService()
        self.serializer = ProgressStatusSerializer()
        self.schema = ProgressStatusSchema()

    @view_config(route_name='get_all_progress_statuses')
    def get_all_progress_statuses(self):
        progress_statuses = self.service.get_all_progress_statuses()
        return self.serializer.convert_list_to_json(progress_statuses)

    @view_config(route_name='add_progress_status')
    def add_progress_status(self):
        progress_status_deserialized = self.schema.deserialize(self.request.json_body)
        progress_status = self.serializer.to_mapped_object(progress_status_deserialized)
        self.service.add_progress_status(progress_status)
        return HTTPCreated(json_body={'id': progress_status.progress_statuses_id})

    @view_config(route_name='delete_progress_status')
    def delete_progress_status(self):
        id_ = self.request.matchdict['id']
        self.service.delete_progress_status_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_progress_status')
    def edit_progress_status(self):
        id_ = self.request.matchdict['id']
        progress_status_deserialized = self.schema.deserialize(self.request.json_body)
        progress_status_deserialized['id'] = id_
        new_progress_status = self.serializer.to_mapped_object(progress_status_deserialized)
        self.service.update_progress_status(new_progress_status)
        return {'id': id_}

    @view_config(route_name='get_progress_status')
    def get_progress_status(self):
        id_ = self.request.matchdict['id']
        progress_status = self.service.get_progress_status_by_id(id_)
        return self.serializer.to_json(progress_status)
