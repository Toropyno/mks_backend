import os
from uuid import uuid4

from mks_backend.repositories.filestorage_repository import FilestorageRepository
from mks_backend.models.filestorage import Filestorage


class FilestorageService(object):
    PROTOCOL_STORAGE = '/tmp/protocols/'

    def __init__(self):
        self.repo = FilestorageRepository()

    def get_filestorage_from_request(self, request_data):
        file = request_data.get('protocolFile')

        id_file_storage = str(uuid4())
        self.repo.create_file(id_file_storage, file.file)

        filestorage = Filestorage(idfilestorage=id_file_storage,
                                  filename=file.filename,
                                  uri='protocols/download/' + id_file_storage,
                                  filesize=file.limit,
                                  mimeType='text/plain',
                                  description='file description',
                                  authorid=1)
        self.repo.add_file(filestorage)
        return filestorage

    @classmethod
    def compare_two_filestorages(cls, new_filestorage, old_filestorage):
        if new_filestorage != old_filestorage:
            path_to_file = FilestorageService.PROTOCOL_STORAGE + old_filestorage
            if os.path.exists(path_to_file):
                os.remove(path_to_file)
            FilestorageRepository.delete_filestorage_by_id(old_filestorage)
