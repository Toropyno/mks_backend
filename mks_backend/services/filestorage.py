from urllib import request as urllib_request
from uuid import uuid4

from webob.compat import cgi_FieldStorage

from mks_backend.models.filestorage import Filestorage
from mks_backend.repositories.construction_object import ConstructionObjectRepository
from mks_backend.repositories.filestorage import FilestorageRepository
from mks_backend.repositories.filestorage_hdd import FilestorageHDD

from mks_backend.errors.filestorage_error import FilestorageError


class FilestorageService:

    def __init__(self):
        self.repo = FilestorageRepository()
        self.hdd = FilestorageHDD()
        self.repo_object = ConstructionObjectRepository()

    def get_filestorage_by_id(self, id):
        return self.repo.get_filestorage_by_id(id)

    def create_filestorage(self, file: cgi_FieldStorage) -> str:
        id_file_storage = str(uuid4())
        self.hdd.create_file(id_file_storage, file)

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

    def get_filename(self, id: str) -> tuple:
        filestorage = self.repo.get_filestorage_by_id(id)
        if not filestorage:
            raise FilestorageError(6)

        return urllib_request.quote(filestorage.filename.encode('utf-8'))

    def get_path_to_file(self, id: str) -> str:
        path_to_file = self.hdd.get_path_to_file(id)
        return path_to_file

    def compare_two_filestorages(self, new_filestorage_id: str, old_filestorage_id: str) -> None:
        if new_filestorage_id != old_filestorage_id:
            self.delete_filestorage_by_id(old_filestorage_id)

    def get_many_file_storages_by_id(self, ids: list) -> list:
        return self.repo.get_many_file_storages_by_id(ids)

    def get_filestorages_by_object(self, object_id: int) -> list:
        construction_object = self.repo_object.get_construction_object_by_id(object_id)
        return [doc.file_storage for doc in construction_object.documents if doc.file_storage]

    def delete_filestorage_by_id(self, id: str) -> None:
        self.hdd.delete_by_id(id)
        self.repo.delete_filestorage_by_id(id)
