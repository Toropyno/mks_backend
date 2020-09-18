from mks_backend.models.construction_document import ConstructionDocument
from mks_backend.repositories.construction_document import ConstructionDocumentRepository
from mks_backend.repositories.filestorage import FilestorageRepository


class ConstructionDocumentService:

    def __init__(self):
        self.repo = ConstructionDocumentRepository()

    def get_all_construction_documents(self) -> list:
        return self.repo.get_all_construction_documents()

    def get_construction_document_by_id(self, id: int) -> ConstructionDocument:
        return self.repo.get_construction_document_by_id(id)

    def add_construction_document(self, construction_document: ConstructionDocument) -> None:
        self.repo.add_construction_document(construction_document)

    def delete_construction_document_by_id_with_filestorage_cascade(self, id: int) -> None:
        construction_document = self.get_construction_document_by_id(id)
        file_storage_id = construction_document.idfilestorage
        self.repo.delete_construction_document(construction_document)
        FilestorageRepository.delete_filestorage_by_id(file_storage_id)

    def update_construction_document(self, construction_document: ConstructionDocument) -> None:
        self.repo.update_construction_document(construction_document)

    def get_many_construction_documents_by_id(self, ids: list) -> list:
        return self.repo.get_many_construction_documents_by_id(ids)
