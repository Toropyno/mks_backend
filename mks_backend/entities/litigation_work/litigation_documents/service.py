from typing import List

from .model import LitigationDocument
from .repository import LitigationDocumentRepository


class LitigationDocumentService:

    def __init__(self):
        self.repo = LitigationDocumentRepository()

    def get_litigation_document_by_id(self, id_: int) -> LitigationDocument:
        return self.repo.get_litigation_document_by_id(id_)

    def add_litigation_document(self, litigation_document: LitigationDocument) -> None:
        self.repo.add_litigation_document(litigation_document)

    def update_litigation_document(self, litigation_document: LitigationDocument) -> None:
        self.repo.update_litigation_document(litigation_document)

    def delete_litigation_document_by_id(self, id_: int) -> None:
        self.repo.delete_litigation_document(id_)

    def get_many_litigation_documents_by_id(self, ids: list) -> List[LitigationDocument]:
        return self.repo.get_many_litigation_documents_by_id(ids)

    def get_litigation_documents_by_litigation(self, litigation_id: int) -> list:
        return self.repo.get_litigation_documents_by_litigation(litigation_id)
