from mks_backend.repositories.filestorage_repository import FilestorageRepository


class FilestorageService(object):
    def __init__(self):
        self.repo = FilestorageRepository()
