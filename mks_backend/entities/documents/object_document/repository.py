from mks_backend.session import DBSession

from .model import ObjectDocument


class ObjectDocumentRepository:

    def __init__(self):
        self._query = DBSession.query(ObjectDocument)

    def update(self):
        DBSession.commit()
