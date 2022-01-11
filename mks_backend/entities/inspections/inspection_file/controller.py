from pyramid.httpexceptions import HTTPNoContent, HTTPCreated
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import InspectionFileSchema
from .service import InspectionFileService
from .serializer import InspectionFileSerializer


@view_defaults(renderer='json')
class InspectionFileController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = InspectionFileSchema()
        self.service = InspectionFileService()
        self.serializer = InspectionFileSerializer()

    @view_config(route_name='get_files_by_inspection')
    def get_files_by_inspection(self):
        id_ = int(self.request.matchdict['inspection_id'])
        inspection_files = self.service.get_files_by_inspection_id(id_)
        return self.serializer.convert_list_to_json(inspection_files)

    @view_config(route_name='add_inspection_file')
    def add_inspection_files(self):
        inspection_files_deserialized = self.schema.deserialize(self.request.json_body)
        inspection_files_deserialized = self.serializer.to_object_list(inspection_files_deserialized)

        self.service.add_inspection_files(inspection_files_deserialized)
        files_ids = [inspection_file.idfilestorage for inspection_file in inspection_files_deserialized]
        return HTTPCreated(json_body={'ids': files_ids})

    @view_config(route_name='delete_inspection_file')
    def delete_inspection_file(self):
        file_id = self.request.matchdict['file_id']
        self.service.delete_inspection_file(file_id)
        return HTTPNoContent()
