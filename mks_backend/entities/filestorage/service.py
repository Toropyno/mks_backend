from urllib import request as urllib_request
from uuid import uuid4

from webob.compat import cgi_FieldStorage

from .model import Filestorage
from .repository import FilestorageRepository
from .hdd import FilestorageHDD

from mks_backend.entities.construction_objects.construction_object import ConstructionObjectService


class FilestorageService:

    def __init__(self):
        self.repo = FilestorageRepository()
        self.hdd = FilestorageHDD()
        self.construction_object_service = ConstructionObjectService()

    def get_filestorage_by_id(self, id_):
        return self.repo.get_filestorage_by_id(id_)

    def create_filestorage(self, file: cgi_FieldStorage, file_format: str = None) -> str:
        id_file_storage = str(uuid4())
        self.hdd.create_file(id_file_storage, file, file_format)

        filestorage = Filestorage(
            idfilestorage=id_file_storage,
            filename=file.filename,
            uri='/file/' + id_file_storage,
            filesize=file.limit,
            mimeType=self.hdd.guess_mime_type(file.filename),
            description='file description',
            authorid=1
        )
        self.repo.add_filestorage(filestorage)

        return id_file_storage

    def get_filename(self, id_: str) -> tuple:
        filestorage = self.repo.get_filestorage_by_id(id_)
        return urllib_request.quote(filestorage.filename.encode('utf-8'))

    def get_path_to_file(self, id_: str) -> str:
        path_to_file = self.hdd.get_path_to_file(id_)
        return path_to_file

    def compare_two_filestorages(self, new_filestorage_id: str, old_filestorage_id: str) -> None:
        if new_filestorage_id != old_filestorage_id:
            self.delete_filestorage_by_id(old_filestorage_id)

    def get_many_file_storages_by_id(self, ids: list) -> list:
        return self.repo.get_many_file_storages_by_id(ids)

    def get_filestorages_by_object(self, object_id: int) -> list:
        construction_object = self.construction_object_service.get_construction_object_by_id(object_id)
        return [doc.file_storage for doc in construction_object.documents if doc.file_storage]

    def delete_filestorage_by_id(self, id_: str) -> None:
        self.repo.delete_filestorage_by_id(id_)
