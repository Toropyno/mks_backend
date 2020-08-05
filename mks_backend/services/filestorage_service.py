from uuid import uuid4

from pyramid.response import FileResponse, Response

from mks_backend.repositories.filestorage_repository import FilestorageRepository
from mks_backend.models.filestorage import Filestorage


class FilestorageService(object):
    def __init__(self):
        self.repo = FilestorageRepository()

    def create_filestorage_from_request(self, request_data):
        file = request_data.get('protocolFile')

        id_file_storage = str(uuid4())
        self.repo.create_file(id_file_storage, file)

        filestorage = Filestorage(idfilestorage=id_file_storage,
                                  filename=file.filename,
                                  uri='protocols/download/' + id_file_storage,
                                  filesize=file.limit,
                                  mimeType=self.repo.guess_mime_type(file.filename),
                                  description='file description',
                                  authorid=1)
        self.repo.add_filestorage(filestorage)
        return filestorage.idfilestorage

    def get_file(self, id):
        path_to_file, filename = self.repo.get_file(id)
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
