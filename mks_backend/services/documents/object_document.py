from mks_backend.models.documents.object_document import ObjectDocument
from mks_backend.repositories.documents.object_document import ObjectDocumentRepository


class ObjectDocumentService:

    def __init__(self):
        self.repo = ObjectDocumentRepository()

    def get_object_document_by_id(self, id: int) -> ObjectDocument:
        return self.repo.get_object_document_by_id(id)

    def add_object_document(self, object_document: ObjectDocument) -> None:
        return self.repo.add_object_document(object_document)

    def delete_object_document_by_id(self, id: int) -> None:
        self.repo.delete_object_document_by_id(id)

    def get_all_object_documents(self) -> list:
        return self.repo.get_all_object_documents()

    def get_object_document_by_relations(self, construction_objects_id: int, construction_documents_id: int):
        return self.repo.get_object_document_by_relations(construction_objects_id, construction_documents_id)
