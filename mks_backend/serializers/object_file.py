from mks_backend.models.object_file import ObjectFile
from mks_backend.serializers.filestorage import FileStorageSerializer
from mks_backend.serializers.utils.date_and_time import get_date_time_string

from mks_backend.errors.serialize_error import serialize_error_handler


class ObjectFileSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, object_file: ObjectFile) -> dict:
        return {
            'id': object_file.object_files_id,
            'file': FileStorageSerializer.to_json(
                object_file.file_storage
            ),
            'constructionObjectId': object_file.construction_objects_id,
            'uploadDate': get_date_time_string(object_file.upload_date),
            'note': object_file.note,
        }

    def convert_list_to_json(self, object_files_list: list) -> list:
        return list(map(self.convert_object_to_json, object_files_list))

    def convert_schema_to_object(self, schema: dict) -> ObjectFile:
        object_file = ObjectFile()

        object_file.object_files_id = schema.get('id')
        object_file.idfilestorage = schema.get('idFileStorage')
        object_file.construction_objects_id = schema.get('constructionObjectId')
        object_file.upload_date = schema.get('uploadDate')
        object_file.note = schema.get('note')

        return object_file
