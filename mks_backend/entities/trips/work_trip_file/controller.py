from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .service import WorkTripFilesService
from .schema import WorkTripFilesShema
from .serializer import WorkTripFilesSerializer


@view_defaults(renderer='json')
class WorkTripFilesController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = WorkTripFilesSerializer()
        self.service = WorkTripFilesService()
        self.schema = WorkTripFilesShema()

    @view_config(route_name='get_all_work_trip_files')
    def get_all_work_trip_files(self):
        work_trip_id = self.request.matchdict['id']
        work_trip_files = self.service.get_all_work_trip_files(work_trip_id)
        return self.serializer.list_to_json(work_trip_files)

    @view_config(route_name='add_work_trip_files')
    def add_work_trip_files(self):
        work_trip_files_deserialized = self.schema.deserialize(self.request.json_body)

        work_trip_files_ids = []

        for work_trip_file_id in work_trip_files_deserialized.get('id'):
            work_trip_file = {
                'id': work_trip_file_id,
                'note': work_trip_files_deserialized.get('note'),
                'workTripId': work_trip_files_deserialized.get('workTripId')
            }
            self.service.add_work_trip_file(self.serializer.to_object(work_trip_file))
            work_trip_files_ids.append(work_trip_file_id)

        return {'id': work_trip_files_ids}

    @view_config(route_name='delete_work_trip_file')
    def delete_work_trip_file(self):
        id_ = self.request.matchdict['id']
        self.service.delete_work_trip_file(id_)
        return {'id': id_}
