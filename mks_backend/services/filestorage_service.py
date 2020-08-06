from uuid import uuid4
from urllib import request as urllib_request

from pyramid.response import FileResponse, Response
from webob.compat import cgi_FieldStorage
from sqlalchemy.exc import DatabaseError

from mks_backend.repositories.filestorage_repository import FilestorageRepository
from mks_backend.repositories.filestorage_hdd import FilestorageHDD, FilestorageException
from mks_backend.models.filestorage import Filestorage


class FilestorageService(object):
    ALLOWED_EXTENSIONS = [
        'doc', 'docx', 'docm',
        'pdf', 'odt', 'txt',
    ]

    def __init__(self):
        self.repo = FilestorageRepository()
        self.hdd = FilestorageHDD()

    def create_filestorage(self, request_data):
        file = request_data.get('protocolFile')

        if not isinstance(file, cgi_FieldStorage):
            raise FilestorageException(1)
        elif file.limit > 2.6e+7:  # > ~25Mbytes
            raise FilestorageException(2)
        elif '.' not in file.filename or \
                file.filename.split('.')[1] not in self.ALLOWED_EXTENSIONS:
            raise FilestorageException(3)

        id_file_storage = str(uuid4())
        self.hdd.create_file(id_file_storage, file)

        filestorage = Filestorage(idfilestorage=id_file_storage,
                                  filename=file.filename,
                                  uri='protocols/download/' + id_file_storage,
                                  filesize=file.limit,
                                  mimeType=self.hdd.guess_mime_type(file.filename),
                                  description='file description',
                                  authorid=1)
        self.repo.add_filestorage(filestorage)
        return filestorage.idfilestorage

    def get_file(self, id):
        try:
            filename = self.repo.get_filestorage_by_id(id).filename
            filename = urllib_request.quote(filename.encode('utf-8'))
        except DatabaseError:
            raise FilestorageException(6)

        path_to_file = self.hdd.get_file(id)
        if path_to_file and filename:
            response = FileResponse(path_to_file)
            response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{filename}"
        else:
            response = Response(f'Unable to find file with id = {id}')
        return response

    @classmethod
    def compare_two_filestorages(cls, new_filestorage, old_filestorage):
        if new_filestorage != old_filestorage:
            FilestorageRepository.delete_filestorage_by_id(old_filestorage)
            FilestorageHDD.delete_by_id(old_filestorage)
