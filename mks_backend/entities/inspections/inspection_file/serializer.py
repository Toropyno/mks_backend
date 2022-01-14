from typing import List

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.filestorage import FileStorageSerializer
from mks_backend.utils.date_and_time import get_date_time_string

from .model import InspectionFile


class InspectionFileSerializer(BaseSerializer):

    def to_json(self, inspection_file: InspectionFile) -> dict:
        return {
            'file': FileStorageSerializer.to_json(inspection_file.file_storage),
            'note': inspection_file.note,
            'uploadDate': get_date_time_string(inspection_file.upload_date)
        }

    def to_object_list(self, schema: dict) -> List[InspectionFile]:
        return [self.to_mapped_object(schema, idfilestorage) for idfilestorage in schema.get('ids', [])]

    def to_mapped_object(self, schema: dict, idfilestorage: str = None) -> InspectionFile:
        return InspectionFile(
            idfilestorage=idfilestorage,
            note=schema.get('note'),
            inspections_id=schema.get('inspectionId'),
        )
