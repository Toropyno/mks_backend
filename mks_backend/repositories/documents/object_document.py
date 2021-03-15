from mks_backend.models.documents.object_document import ObjectDocument
from mks_backend.session import DBSession


class ObjectDocumentRepository:

    def __init__(self):
        self._query = DBSession.query(ObjectDocument)

    def get_object_documents_by_object_id(self, object_id: int):
        return self._query.filter(ObjectDocument.construction_objects_id == object_id).all()

    def update(self):
        DBSession.commit()
