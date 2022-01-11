from pyramid.httpexceptions import HTTPNoContent, HTTPCreated
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ConstructionProgressSchema
from .serializer import ConstructionProgressSerializer
from .service import ConstructionProgressService


@view_defaults(renderer='json')
class ConstructionProgressController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionProgressSerializer()
        self.service = ConstructionProgressService()
        self.schema = ConstructionProgressSchema()

    @view_config(route_name='add_construction_progress')
    def add_construction_progress(self):
        construction_progress_deserialized = self.schema.deserialize(self.request.json_body)
        construction_progress = self.serializer.to_mapped_object(construction_progress_deserialized)
        self.service.add_construction_progress(construction_progress)
        return HTTPCreated(json_body={'id': construction_progress.construction_progress_id})

    @view_config(route_name='get_construction_progress')
    def get_construction_progress(self):
        id_ = int(self.request.matchdict['id'])
        construction_progress = self.service.get_construction_progress_by_id(id_)
        return self.serializer.to_json(construction_progress)

    @view_config(route_name='delete_construction_progress')
    def delete_construction_progress(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_progress_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_construction_progress')
    def edit_construction_progress(self):
        id_ = int(self.request.matchdict['id'])
        construction_progress_deserialized = self.schema.deserialize(self.request.json_body)

        construction_progress_deserialized['id'] = id_
        construction_progress = self.serializer.to_mapped_object(construction_progress_deserialized)

        self.service.update_construction_progress(construction_progress)
        return {'id': id_}

    @view_config(route_name='get_all_construction_progresses_by_object')
    def get_all_construction_progresses_by_object(self):
        object_id = int(self.request.matchdict['id'])
        construction_progresses = self.service.get_all_construction_progresses_by_object(object_id)
        construction_progresses = self.serializer.convert_list_to_json(construction_progresses)
        return construction_progresses

    @view_config(route_name='get_last_construction_progress_by_object')
    def get_last_construction_progress_by_object(self):
        object_id = int(self.request.matchdict['id'])
        construction_progress = self.service.get_last_construction_progress_by_object(object_id)
        return self.serializer.to_json(construction_progress)
