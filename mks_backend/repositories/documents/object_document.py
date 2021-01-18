from mks_backend.models.documents.object_document import ObjectDocument
from mks_backend.session import DBSession


class ObjectDocumentRepository:

    def __init__(self):
        self._query = DBSession.query(ObjectDocument)

    def get_all_object_documents(self) -> list:
        return self._query.all()

    def add_object_document(self, object_document: ObjectDocument) -> None:
        DBSession.add(object_document)
        DBSession.commit()

    def delete_object_document_by_id(self, id: int) -> None:
        self._query.filter_by(object_documents_id=id).delete()
        DBSession.commit()

    def get_object_document_by_id(self, id: int) -> ObjectDocument:
        return self._query.get(id)

    def get_object_document_by_relations(self, construction_objects_id: int, construction_documents_id: int):
        return self._query.filter(
            ObjectDocument.construction_objects_id == construction_objects_id,
            ObjectDocument.construction_documents_id == construction_documents_id
        ).first()
