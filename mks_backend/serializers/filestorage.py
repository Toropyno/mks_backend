from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.filestorage import Filestorage
from mks_backend.serializers.utils.date_and_time import get_date_time_zone


class FileStorageSerializer:

    @classmethod
    @serialize_error_handler
    def to_json(cls, filestorage: Filestorage):
        return {
            'idFileStorage': str(filestorage.idfilestorage),
            'name': filestorage.filename,
            'size': filestorage.size,
            'createdOn': get_date_time_zone(filestorage.createdOn),
        }

    def convert_list_to_json(self, filestorages: list) -> list:
        return list(map(self.to_json, filestorages))
