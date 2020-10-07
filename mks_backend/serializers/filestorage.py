from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.filestorage import Filestorage
from mks_backend.serializers.utils.date_and_time import get_date_time_zone


class FileStorageSerializer:

    @classmethod
    # @serialize_error_handler
    def convert_object_to_json(cls, filestorage: Filestorage, file_info=None) -> dict:
        return {
            'id': str(filestorage.idfilestorage),
            'fileName': file_info.get('filename'),
            'uri': filestorage.uri,
            'size': file_info.get('filesize'),
            'mimeType': filestorage.mimeType,
            'createdOn': get_date_time_zone(filestorage.createdOn),
            'description': filestorage.description,
            'authorId': filestorage.authorid,
        }

    def convert_list_to_json(self, filestorages: list) -> list:
        return list(map(self.convert_object_to_json, filestorages))

    @classmethod
    def convert_file_info_with_idfilestorage(cls, idfilestorage, file_info):
        if file_info:
            return {
                'idFileStorage': idfilestorage,
                'name': file_info.get('filename'),
                'size': file_info.get('filesize'),
            }
