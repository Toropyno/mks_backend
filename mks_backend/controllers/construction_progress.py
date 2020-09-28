from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.controllers.schemas.construction_progress import ConstructionProgressSchema
from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
from mks_backend.serializers.construction_progress import ConstructionProgressSerializer
from mks_backend.services.construction_progress import ConstructionProgressService


class ConstructionProgressController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionProgressSerializer()
        self.service = ConstructionProgressService()
        self.schema = ConstructionProgressSchema()

    @view_config(route_name='get_all_construction_progresses', renderer='json')
    def get_all_construction_progresses(self):
        construction_progresses = self.service.get_all_construction_progresses()
        return self.serializer.convert_list_to_json(construction_progresses)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_construction_progress', renderer='json')
    def add_construction_progress(self):
        construction_progress_deserialized = self.schema.deserialize(self.request.json_body)

        construction_progress = self.serializer.convert_schema_to_object(construction_progress_deserialized)
        self.service.add_construction_progress(construction_progress)
        return {'id': construction_progress.construction_progress_id}

    @view_config(route_name='get_construction_progress', renderer='json')
    def get_construction_progress(self):
        id = int(self.request.matchdict['id'])
        construction_progress = self.service.get_construction_progress_by_id(id)
        return self.serializer.convert_object_to_json(construction_progress)

    @view_config(route_name='delete_construction_progress', renderer='json')
    def delete_construction_progress(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_progress_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_construction_progress', renderer='json')
    def edit_construction_progress(self):
        id = int(self.request.matchdict['id'])
        construction_progress_deserialized = self.schema.deserialize(self.request.json_body)

        construction_progress_deserialized['id'] = id
        construction_progress = self.serializer.convert_schema_to_object(construction_progress_deserialized)

        self.service.update_construction_progress(construction_progress)
        return {'id': id}
