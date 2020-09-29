from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.repositories.construction_object import ConstructionObjectRepository
from mks_backend.repositories.documents.construction_document import ConstructionDocumentRepository
from mks_backend.repositories.filestorage import FilestorageRepository


class ConstructionDocumentService:

    def __init__(self):
        self.repo = ConstructionDocumentRepository()
        self.repo_object = ConstructionObjectRepository()

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
        if file_storage_id:
            FilestorageRepository.delete_filestorage_by_id(file_storage_id)

    def update_construction_document(self, construction_document: ConstructionDocument) -> None:
        self.repo.update_construction_document(construction_document)

    def get_many_construction_documents_by_id(self, ids: list) -> list:
        return self.repo.get_many_construction_documents_by_id(ids)

    def get_construction_documents_by_object(self, object_id: int) -> list:
        construction_object = self.repo_object.get_construction_object_by_id(object_id)
        if construction_object:
            return construction_object.documents
        return []

    def get_construction_documents_by_construction(self, construction_id: int) -> list:
        construction_documents = self.repo.get_construction_documents_by_construction(construction_id)
        if construction_documents:
            return construction_documents
        return []
