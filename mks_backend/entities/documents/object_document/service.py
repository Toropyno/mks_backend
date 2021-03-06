from typing import List

from mks_backend.entities.construction_objects.construction_object import ConstructionObjectService
from mks_backend.entities.documents.construction_document import ConstructionDocumentService

from .repository import ObjectDocumentRepository


class ObjectDocumentService:

    def __init__(self):
        self.repo = ObjectDocumentRepository()
        self.object_service = ConstructionObjectService()
        self.construction_documents_service = ConstructionDocumentService()

    def get_documents_by_construction_object(self, object_id: int) -> List:
        construction_object = self.object_service.get_construction_object_by_id(object_id)
        return construction_object.documents

    def edit_construction_document_and_object_relations(self, object_id: int, construction_documents_ids: List[int]):
        construction_object = self.object_service.get_construction_object_by_id(object_id)
        construction_documents = self.construction_documents_service.\
            get_many_construction_documents_by_id(construction_documents_ids)

        construction_object.documents = construction_documents
        self.repo.update()
