from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.repositories.construction_object import ConstructionObjectRepository
from mks_backend.repositories.documents.construction_document import ConstructionDocumentRepository
from mks_backend.services.documents.upload_date_utils import set_upload_date_by_idfilestorage


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

    def update_construction_document(self, construction_document: ConstructionDocument) -> None:
        self.repo.update_construction_document(construction_document)

    def delete_construction_document_by_id(self, id: int) -> None:
        self.repo.delete_construction_document(id)

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

    def convert_schema_to_object(self, schema_dict: dict, old_construction_document=None) -> ConstructionDocument:
        construction_document = ConstructionDocument()

        construction_document.idfilestorage = schema_dict.get('idFileStorage')
        set_upload_date_by_idfilestorage(construction_document, old_construction_document)

        construction_document.construction_documents_id = schema_dict.get('id')
        construction_document.construction_id = schema_dict.get('constructionId')
        construction_document.doctypes_id = schema_dict.get('docTypesId')
        construction_document.doc_number = schema_dict.get('docNumber')
        construction_document.doc_date = schema_dict.get('docDate')
        construction_document.doc_name = schema_dict.get('docName')
        construction_document.note = schema_dict.get('note')

        return construction_document
