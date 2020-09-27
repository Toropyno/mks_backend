from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.filestorage import Filestorage
from mks_backend.serializers.utils.date_and_time import get_date_time_zone
from mks_backend.services.filestorage import FilestorageService


class FileStorageSerializer:

    @classmethod
    @serialize_error_handler
    def convert_file_info_to_json(cls, id) -> dict:
        file_info = FilestorageService().get_file_info(id)
        return {
            'idFileStorage': id,
            'name': file_info.get('filename'),
            'size': file_info.get('filesize'),
        }

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, file_storage: Filestorage) -> dict:
        file_info = FilestorageService().get_file_info(file_storage.idfilestorage)
        return {
            'id': file_storage.idfilestorage,
            'fileName': file_info.get('filename'),
            'uri': file_storage.uri,
            'size': file_info.get('filesize'),
            'mimeType': file_storage.mimeType,
            'createdOn': get_date_time_zone(file_storage.createdOn),
            # 'description': file_storage.description,
            # 'authorId': file_storage.authorid,
        }

    def convert_list_to_json(self, file_storages: list) -> list:
        return list(map(self.convert_object_to_json, file_storages))
