from .model import Filestorage

from mks_backend.utils.date_and_time import get_date_time_zone
from mks_backend.errors import serialize_error_handler


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