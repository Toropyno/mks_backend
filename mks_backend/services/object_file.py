from mks_backend.models.object_file import ObjectFile
from mks_backend.repositories.object_file import ObjectFileRepository
from mks_backend.services.filestorage import FilestorageService


class ObjectFileService:

    def __init__(self):
        self.repo = ObjectFileRepository()
        self.service_filestorage = FilestorageService()

    def get_fields_all_object_files(self) -> list:
        return self.repo.get_fields_all_object_files()

    def get_object_file_by_id(self, id: int) -> ObjectFile:
        return self.repo.get_object_file_by_id(id)

    def get_all_object_files(self) -> list:
        return self.repo.get_fields_all_object_files()

    def add_object_file(self, object_file: ObjectFile) -> None:
        self.repo.add_object_file(object_file)

    def update_object_file(self, new_object_file: ObjectFile) -> None:
        self.repo.update_object_file(new_object_file)

    def delete_object_file_by_id(self, id: int) -> None:
        self.repo.delete_object_file_by_id(id)

    def set_upload_date(self, object_file_deserialized):
        filestorage = self.service_filestorage.get_filestorage_by_id(object_file_deserialized['idFileStorage'])
        object_file_deserialized['uploadDate'] = filestorage.createdOn
