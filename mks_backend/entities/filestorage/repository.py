from mks_backend.session import DBSession
from .model import Filestorage

from mks_backend.errors.filestorage_error import FilestorageError


class FilestorageRepository:

    def __init__(self):
        self._query = DBSession.query(Filestorage)

    def add_filestorage(self, file: Filestorage):
        DBSession.add(file)
        DBSession.commit()

    def get_filestorage_by_id(self, id: str) -> Filestorage:
        filestorage = self._query.get(id)
        if not filestorage:
            raise FilestorageError('nf_in_db')
        return filestorage

    def delete_filestorage_by_id(self, id: str) -> None:
        self._query.filter_by(idfilestorage=id).delete()
        DBSession.commit()

    def get_many_file_storages_by_id(self, ids: list) -> list:
        return self._query.filter(
            Filestorage.idfilestorage.in_(ids)
        ).all()
