from mks_backend.entities.filestorage import FilestorageService
from mks_backend.session import Base


class UploadDateService:

    def __init__(self):
        self.service_filestorage = FilestorageService()

    def set_upload_date_by_idfilestorage(self, document: Base) -> None:
        if document.idfilestorage:
            document.upload_date = self.service_filestorage.get_filestorage_by_id(document.idfilestorage).createdOn
