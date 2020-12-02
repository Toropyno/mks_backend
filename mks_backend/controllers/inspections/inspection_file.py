from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.inspections.inspection_file import InspectionFileSchema
from mks_backend.services.inspections.inspection_file import InspectionFileService
from mks_backend.serializers.inspections.inspection_file import InspectionFileSerializer

from mks_backend.errors import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class InspectionFileController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = InspectionFileSchema()
        self.service = InspectionFileService()
        self.serializer = InspectionFileSerializer()

    @view_config(route_name='get_files_by_inspection')
    def get_files_by_inspection(self):
        id = int(self.request.matchdict['inspection_id'])
        inspection_files = self.service.get_files_by_inspection_id(id)
        return self.serializer.convert_list_to_json(inspection_files)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_inspection_file')
    def add_inspection_file(self):
        inspection_deserialized = self.schema.deserialize(self.request.json_body)
        inspection = self.serializer.to_object(inspection_deserialized)

        self.service.add_inspection_file(inspection)
        return {'id': inspection.inspections_id}

    @handle_db_error
    @view_config(route_name='delete_inspection_file')
    def delete_inspection_file(self):
        inspection_id = int(self.request.matchdict['inspection_id'])
        file_id = self.request.matchdict['file_id']

        self.service.delete_inspection_file(file_id)
        return {'id': inspection_id}
