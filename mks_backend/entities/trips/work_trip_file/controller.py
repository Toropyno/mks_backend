from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import WorkTripFilesShema
from .serializer import WorkTripFilesSerializer
from .service import WorkTripFilesService


@view_defaults(renderer='json')
class WorkTripFilesController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = WorkTripFilesSerializer()
        self.service = WorkTripFilesService()
        self.schema = WorkTripFilesShema()

    @view_config(route_name='get_all_work_trip_files_by_work_trip_id')
    def get_all_work_trip_files_by_work_trip_id(self):
        work_trip_id = self.request.matchdict['id']
        work_trip_files = self.service.get_all_work_trip_files_by_work_trip_id(work_trip_id)
        return self.serializer.convert_list_to_json(work_trip_files)

    @view_config(route_name='add_work_trip_files')
    def add_work_trip_files(self):
        work_trip_files_deserialized = self.schema.deserialize(self.request.json_body)
        work_trip_files_deserialized = self.serializer.to_object_list(work_trip_files_deserialized)

        self.service.add_work_trip_file(work_trip_files_deserialized)
        files_ids = [work_trip_file.idfilestorage for work_trip_file in work_trip_files_deserialized]
        return HTTPCreated(json_body={'id': files_ids})

    @view_config(route_name='delete_work_trip_file')
    def delete_work_trip_file(self):
        id_ = self.request.matchdict['id']
        self.service.delete_work_trip_file(id_)
        return HTTPNoContent()
