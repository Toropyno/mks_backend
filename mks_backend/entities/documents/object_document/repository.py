from .model import ObjectDocument
from mks_backend.session import DBSession


class ObjectDocumentRepository:

    def __init__(self):
        self._query = DBSession.query(ObjectDocument)

    def update(self):
        DBSession.commit()
