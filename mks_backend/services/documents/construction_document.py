from datetime import datetime

from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.repositories.construction_object import ConstructionObjectRepository
from mks_backend.repositories.documents.construction_document import ConstructionDocumentRepository


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

    def delete_construction_document_by_id_with_filestorage_cascade(self, id: int) -> None:
        construction_document = self.get_construction_document_by_id(id)
        self.repo.delete_construction_document(construction_document)

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

    def set_upload_date_now(self, construction_document_deserialized):
        construction_document_deserialized['uploadDate'] = datetime.now()

    def convert_schema_to_object(self, schema_dict: dict, old_idfilestorage=None) -> ConstructionDocument:
        construction_document = ConstructionDocument()

        construction_document.idfilestorage = schema_dict.get('idFileStorage')
        construction_document.upload_date = schema_dict.get('uploadDate')
        if old_idfilestorage:
            construction_document = self.update_idfilestorage_with_upload_date(construction_document, old_idfilestorage)

        construction_document.construction_documents_id = schema_dict.get('id')
        construction_document.construction_id = schema_dict.get('constructionId')
        construction_document.doctypes_id = schema_dict.get('docTypesId')
        construction_document.doc_number = schema_dict.get('docNumber')
        construction_document.doc_date = schema_dict.get('docDate')
        construction_document.doc_name = schema_dict.get('docName')
        construction_document.note = schema_dict.get('note')

        return construction_document

    def update_idfilestorage_with_upload_date(self, construction_document, old_idfilestorage):
        schema_idfilestorage = construction_document.idfilestorage
        if old_idfilestorage:
            if str(old_idfilestorage) != str(schema_idfilestorage):
                construction_document.idfilestorage = schema_idfilestorage
                construction_document.upload_date = datetime.now()
        else:
            if schema_idfilestorage:
                construction_document.upload_date = datetime.now()
        return construction_document
