from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.object_document import ObjectDocument
from mks_backend.repositories import DBSession


class ObjectDocumentRepository:

    def get_all_object_documents(self) -> list:
        return DBSession.query(ObjectDocument).all()

    @db_error_handler
    def add_object_document(self, object_document: ObjectDocument) -> None:
        DBSession.add(object_document)
        DBSession.commit()

    def delete_object_document_by_id(self, id: int) -> None:
        object_document = self.get_object_document_by_id(id)
        DBSession.delete(object_document)
        DBSession.commit()

    def get_object_document_by_id(self, id: int) -> ObjectDocument:
        return DBSession.query(ObjectDocument).get(id)

    def get_object_document_by_relations(self, construction_objects_id: int, construction_documents_id: int):
        return DBSession.query(ObjectDocument).filter(
            ObjectDocument.construction_objects_id == construction_objects_id,
            ObjectDocument.construction_documents_id == construction_documents_id
        ).first()
