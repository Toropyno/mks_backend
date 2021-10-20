from sqlalchemy.event import listens_for

from mks_backend.entities.filestorage import FilestorageService
from mks_backend.models_meta import WorkTripFiles


@listens_for(WorkTripFiles, 'before_insert')
def set_upload_date_before_insert(mapper, connection, instance: WorkTripFiles):
    instance.upload_date = FilestorageService().get_filestorage_by_id(instance.idfilestorage).createdOn
