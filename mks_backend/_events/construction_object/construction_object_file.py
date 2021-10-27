from sqlalchemy.event import listens_for

from mks_backend.entities.filestorage import FilestorageService
from mks_backend.entities.construction_objects.object_file.model import ObjectFile


@listens_for(ObjectFile, 'before_insert')
def set_upload_date_before_insert(mapper, connection, instance: ObjectFile):
    instance.upload_date = FilestorageService().get_filestorage_by_id(instance.idfilestorage).createdOn
