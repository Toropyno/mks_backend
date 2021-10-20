from mks_backend.errors import serialize_error_handler
from mks_backend.utils.date_and_time import get_date_time_string
from .model import WorkTripFiles


class WorkTripFilesSerializer:

    @serialize_error_handler
    def to_json(self, work_trip_file: WorkTripFiles) -> dict:
        return {
            'id': work_trip_file.idfilestorage,
            'note': work_trip_file.note,
            'uploadDate': get_date_time_string(work_trip_file.upload_date),
            'fileName': work_trip_file.file_storage.filename,
            'fileSize': work_trip_file.file_storage.size
        }

    def to_object(self, schema: dict) -> WorkTripFiles:
        work_trip_file = WorkTripFiles()

        work_trip_file.idfilestorage = schema.get('id')
        work_trip_file.note = schema.get('note')
        work_trip_file.work_trips_id = schema.get('workTripId')

        return work_trip_file

    def list_to_json(self, work_trip_files_list: list) -> list:
        return list(map(self.to_json, work_trip_files_list))
