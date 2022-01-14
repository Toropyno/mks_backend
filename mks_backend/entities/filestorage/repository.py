from mks_backend.errors.filestorage_error import FilestorageError
from mks_backend.session import DBSession

from .model import Filestorage


class FilestorageRepository:

    def __init__(self):
        self._query = DBSession.query(Filestorage)

    def add_filestorage(self, file: Filestorage):
        DBSession.add(file)
        DBSession.commit()

    def get_filestorage_by_id(self, id_: str) -> Filestorage:
        filestorage = self._query.get(id_)
        if not filestorage:
            raise FilestorageError('nf_in_db')
        return filestorage

    def delete_filestorage_by_id(self, id_: str) -> None:
        self._query.filter_by(idfilestorage=id_).delete()
        DBSession.commit()

    def get_many_file_storages_by_id(self, ids: list) -> list:
        return self._query.filter(
            Filestorage.idfilestorage.in_(ids)
        ).all()
