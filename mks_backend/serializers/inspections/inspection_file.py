from typing import List

from mks_backend.models.inspections.inspection_file import InspectionFile
from mks_backend.serializers.filestorage import FileStorageSerializer
from mks_backend.serializers.utils.date_and_time import get_date_time_string


class InspectionFileSerializer:

    def to_json(self, inspection_file: InspectionFile) -> dict:
        file_storage = FileStorageSerializer.to_json(inspection_file.file_storage)
        file_storage.update({
            'note': inspection_file.note,
            'upload_date': get_date_time_string(inspection_file.upload_date)
        })

        return file_storage

    def convert_list_to_json(self, inspection_files: List[InspectionFile]) -> List[dict]:
        return list(map(self.to_json, inspection_files))

    def to_object(self, schema: dict) -> InspectionFile:
        inspection_file = InspectionFile()

        inspection_file.idfilestorage = schema.get('idFileStorage')
        inspection_file.inspections_id = schema.get('inspection')
        inspection_file.note = schema.get('note')

        return inspection_file
