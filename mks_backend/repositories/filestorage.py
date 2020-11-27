from mks_backend.models import DBSession
from mks_backend.models.filestorage import Filestorage


class FilestorageRepository:

    def __init__(self):
        self._query = DBSession.query(Filestorage)

    def add_filestorage(self, file: Filestorage):
        DBSession.add(file)
        DBSession.commit()

    def get_filestorage_by_id(self, id: str) -> Filestorage:
        return self._query.get(id)

    def delete_filestorage_by_id(self, id: str) -> None:
        self._query.filter_by(idfilestorage=id).delete()
        DBSession.commit()

    def get_many_file_storages_by_id(self, ids: list) -> list:
        return self._query.filter(
            Filestorage.idfilestorage.in_(ids)
        ).all()
