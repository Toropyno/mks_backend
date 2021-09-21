from sqlalchemy.event import listens_for

from .model import Filestorage
from .hdd import FilestorageHDD


@listens_for(Filestorage, 'after_delete')
def delete_filestorage_from_hdd(mapper, connection, instance: Filestorage):
    hdd_service = FilestorageHDD()
    hdd_service.delete_by_id(str(instance.idfilestorage))
