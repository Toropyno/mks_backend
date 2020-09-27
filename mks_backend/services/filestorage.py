from urllib import request as urllib_request
from uuid import uuid4

from pyramid.response import FileResponse, Response
from sqlalchemy.exc import DatabaseError
from webob.compat import cgi_FieldStorage
from webob.multidict import MultiDict

from mks_backend.errors.filestorage_error import FilestorageError
from mks_backend.models.filestorage import Filestorage
from mks_backend.repositories.filestorage import FilestorageRepository
from mks_backend.repositories.filestorage_hdd import FilestorageHDD


class FilestorageService:
    ALLOWED_EXTENSIONS = [
        'doc', 'docx', 'docm',
        'pdf', 'odt', 'txt',
    ]

    def __init__(self):
        self.repo = FilestorageRepository()
        self.hdd = FilestorageHDD()

    def create_filestorage(self, request_data: MultiDict) -> str:
        file = request_data.get('protocolFile')

        if not isinstance(file, cgi_FieldStorage):
            raise FilestorageError(1)
        elif file.limit > 2.6e+7:  # > ~25Mbytes
            raise FilestorageError(2)
        elif '.' not in file.filename or \
                file.filename.split('.')[1] not in self.ALLOWED_EXTENSIONS:
            raise FilestorageError(3)

        id_file_storage = str(uuid4())
        self.hdd.create_file(id_file_storage, file)

        filestorage = Filestorage(idfilestorage=id_file_storage,
                                  filename=file.filename,
                                  uri='protocol/download/' + id_file_storage,
                                  filesize=file.limit,
                                  mimeType=self.hdd.guess_mime_type(file.filename),
                                  description='file description',
                                  authorid=1)
        self.repo.add_filestorage(filestorage)
        return filestorage.idfilestorage

    def get_file(self, id: int) -> Response:
        try:
            filename = self.repo.get_filestorage_by_id(id).filename
            filename = urllib_request.quote(filename.encode('utf-8'))
        except DatabaseError:
            raise FilestorageError(6)

        path_to_file = self.hdd.get_file(id)
        if path_to_file and filename:
            response = FileResponse(path_to_file)
            response.headers['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(filename)
        else:
            response = Response('Unable to find file with id = {}'.format(id))
        return response

    def get_file_info(self, uuid):
        try:
            filestorage = self.repo.get_filestorage_by_id(uuid)
        except DatabaseError:
            raise FilestorageError(6)

        filename = filestorage.filename
        filesize = filestorage.filesize / 1024  # to Kbytes

        if filesize >= 1024:
            filesize = filesize / 1024
            filesize = '{:.1f}Мб'.format(filesize)
        else:
            filesize = '{:.1f}Кб'.format(filesize)

        return {
            'filename': filename,
            'filesize': filesize
        }

    @classmethod
    def compare_two_filestorages(cls, new_filestorage_id: int, old_filestorage_id: int) -> None:
        if new_filestorage_id != old_filestorage_id:
            FilestorageRepository.delete_filestorage_by_id(old_filestorage_id)
            FilestorageHDD.delete_by_id(old_filestorage_id)

    def get_many_file_storages_by_id(self, ids: list) -> list:
        return self.repo.get_many_file_storages_by_id(ids)
