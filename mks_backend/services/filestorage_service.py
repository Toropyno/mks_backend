import os

from mks_backend.repositories.filestorage_repository import FilestorageRepository


class FilestorageService(object):
    PROTOCOL_STORAGE = '/tmp/protocols/'

    def __init__(self):
        self.repo = FilestorageRepository()

    @staticmethod
    def compare_two_filestorages(new_filestorage, old_filestorage):
        if new_filestorage != old_filestorage:
            path_to_file = FilestorageService.PROTOCOL_STORAGE + old_filestorage
            if os.path.exists(path_to_file):
                os.remove(path_to_file)
            FilestorageRepository.delete_protocol_by_id(old_filestorage)
