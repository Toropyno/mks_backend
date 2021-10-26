from typing import Dict, List

from mks_backend.errors import serialize_error_handler
from mks_backend.utils.date_and_time import get_date_time_string
from .model import WorkTripFile


class WorkTripFilesSerializer:

    def list_to_json(self, work_trip_files: List[WorkTripFile]) -> List[Dict]:
        return list(map(self.to_json, work_trip_files))

    @serialize_error_handler
    def to_json(self, work_trip_file: WorkTripFile) -> dict:
        return {
            'id': work_trip_file.idfilestorage,
            'note': work_trip_file.note,
            'uploadDate': get_date_time_string(work_trip_file.upload_date),
            'fileName': work_trip_file.file_storage.filename,
            'fileSize': work_trip_file.file_storage.size
        }

    def to_object_list(self, schema: dict) -> List[WorkTripFile]:
        return [self.to_object(schema, idfilestorage) for idfilestorage in schema.get('id', [])]

    def to_object(self, schema: dict, idfilestorage: str = None) -> WorkTripFile:
        return WorkTripFile(
            idfilestorage=idfilestorage,
            note=schema.get('note'),
            work_trips_id=schema.get('workTripId'),
        )
