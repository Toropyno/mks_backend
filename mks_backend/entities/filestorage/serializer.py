from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler
from mks_backend.utils.date_and_time import get_date_time_zone

from .model import Filestorage


class FileStorageSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, filestorage: Filestorage):
        return {
            'idFileStorage': str(filestorage.idfilestorage),
            'name': filestorage.filename,
            'size': filestorage.size,
            'createdOn': get_date_time_zone(filestorage.createdOn),
        }
