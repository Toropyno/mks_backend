from mks_backend.models.object_file import ObjectFile
from mks_backend.repositories.object_file import ObjectFileRepository


class ObjectFileService:

    def __init__(self):
        self.repo = ObjectFileRepository()

    def get_fields_all_object_files(self) -> list:
        return self.repo.get_fields_all_object_files()

    def get_object_file_by_id(self, id: int) -> ObjectFile:
        return self.repo.get_object_file_by_id(id)

    def add_object_file(self, object_file: ObjectFile) -> None:
        self.repo.add_object_file(object_file)

    def delete_object_file_by_id(self, id: int) -> None:
        object_file = self.get_object_file_by_id(id)
        self.repo.delete_object_file(object_file)

    def get_object_file_by_relations(self, file_storage_id: int, construction_objects_id: int) -> ObjectFile:
        return self.repo.get_object_file_by_relations(file_storage_id, construction_objects_id)
