from mks_backend.models.miv.storage import Storage
from mks_backend.models import DBSession


class StorageRepository:

    def __init__(self):
        self._query = DBSession.query(Storage)

    def add_storage(self, storage: Storage):
        DBSession.add(storage)
        DBSession.commit()
