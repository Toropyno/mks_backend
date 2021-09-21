from .model import ObjectFile
from .repository import ObjectFileRepository

from mks_backend.entities.construction_objects.construction_object import ConstructionObjectService
from mks_backend.entities.filestorage import FilestorageService


class ObjectFileService:

    def __init__(self):
        self.repo = ObjectFileRepository()
        self.service_filestorage = FilestorageService()
        self.service_object = ConstructionObjectService()

    def get_all_object_files(self) -> list:
        return self.repo.get_all_object_files()

    def get_object_file_by_id(self, id: int) -> ObjectFile:
        return self.repo.get_object_file_by_id(id)

    def add_object_file(self, object_file: ObjectFile) -> None:
        self.repo.add_object_file(object_file)

    def update_object_file(self, new_object_file: ObjectFile) -> None:
        self.repo.update_object_file(new_object_file)

    def delete_object_file_by_id(self, id_: int) -> None:
        self.repo.delete_object_file_by_id(id_)

    def set_upload_date(self, object_file_deserialized):
        filestorage = self.service_filestorage.get_filestorage_by_id(object_file_deserialized['idFileStorage'])
        object_file_deserialized['uploadDate'] = filestorage.createdOn

    def get_object_files_by_object(self, object_id: int) -> list:
        construction_object = self.service_object.get_construction_object_by_id(object_id)
        return construction_object.object_files
