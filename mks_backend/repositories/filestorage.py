from mks_backend.models import DBSession
from mks_backend.models.filestorage import Filestorage


class FilestorageRepository:

    def add_filestorage(self, file: Filestorage):
        DBSession.add(file)
        DBSession.commit()

    def get_filestorage_by_id(self, id: str) -> Filestorage:
        return DBSession.query(Filestorage).get(id)

    def delete_filestorage_by_id(self, id: str) -> None:
        filestorage = self.get_filestorage_by_id(id)
        DBSession.delete(filestorage)
        DBSession.commit()

    def get_many_file_storages_by_id(self, ids: list) -> list:
        return DBSession.query(Filestorage).filter(
            Filestorage.idfilestorage.in_(ids)
        ).all()
