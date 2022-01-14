from typing import List

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.filestorage import FileStorageSerializer
from mks_backend.errors import serialize_error_handler
from mks_backend.utils.date_and_time import get_date_time_string

from .model import ObjectFile


class ObjectFileSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, object_file: ObjectFile) -> dict:
        return {
            'id': object_file.object_files_id,
            'file': FileStorageSerializer.to_json(
                object_file.file_storage
            ),
            'constructionObjectId': object_file.construction_objects_id,
            'uploadDate': get_date_time_string(object_file.upload_date),
            'note': object_file.note,
        }

    def to_object_list(self, schema: dict) -> List[ObjectFile]:
        return [self.to_mapped_object(schema, idfilestorage) for idfilestorage in schema.get('idsFileStorage', [])]

    def to_mapped_object(self, schema: dict, idfilestorage: str = None) -> ObjectFile:
        return ObjectFile(
            idfilestorage=idfilestorage,
            note=schema.get('note'),
            construction_objects_id=schema.get('constructionObjectId'),
        )
