from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.object_file import ObjectFile
from mks_backend.serializers.utils.date_and_time import get_date_time_string


class ObjectFileSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, object_file: ObjectFile) -> dict:
        object_file_dict = {
            'id': object_file.object_files_id,
            'idFileStorage': object_file.idfilestorage,
            'constructionObjects': object_file.construction_objects_id,
            'uploadDate': get_date_time_string(object_file.upload_date),
            'note': object_file.upload_date,
        }
        return object_file_dict

    def convert_list_to_json(self, object_files_list: list) -> list:
        return list(map(self.convert_object_to_json, object_files_list))
