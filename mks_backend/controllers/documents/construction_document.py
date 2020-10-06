from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.controllers.schemas.construction_document import ConstructionDocumentSchema
from mks_backend.serializers.documents.construction_document import ConstructionDocumentSerializer
from mks_backend.services.documents.construction_document import ConstructionDocumentService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
from mks_backend.services.filestorage import FilestorageService


class ConstructionDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionDocumentSerializer()
        self.service = ConstructionDocumentService()
        self.schema = ConstructionDocumentSchema()
        self.service_filestorage = FilestorageService()

    @view_config(route_name='get_all_construction_documents', renderer='json')
    def get_all_construction_documents(self):
        construction_documents = self.service.get_all_construction_documents()
        documents = self.get_construction_documents_with_file_info(construction_documents)
        return documents

    @view_config(route_name='get_construction_document', renderer='json')
    def get_construction_document(self):
        id = int(self.request.matchdict['id'])
        construction_document = self.service.get_construction_document_by_id(id)
        file_info = self.service_filestorage.get_file_info_if_idfilestorage(construction_document.idfilestorage)
        return self.serializer.convert_object_to_json(construction_document, file_info)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_construction_document', renderer='json')
    def add_construction_document(self):
        construction_document_deserialized = self.schema.deserialize(self.request.json_body)
        self.service.set_upload_date_now(construction_document_deserialized)
        construction_document = self.service.convert_schema_to_object(construction_document_deserialized)

        self.service.add_construction_document(construction_document)
        return {'id': construction_document.construction_documents_id}

    @view_config(route_name='delete_construction_document', renderer='json')
    def delete_construction_document(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_document_by_id_with_filestorage_cascade(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_construction_document', renderer='json')
    def edit_construction_document(self):
        id = int(self.request.matchdict['id'])
        construction_document_deserialized = self.schema.deserialize(self.request.json_body)

        old_construction_document = self.service.get_construction_document_by_id(id)

        construction_document_deserialized['id'] = id
        construction_document_deserialized['uploadDate'] = old_construction_document.upload_date

        construction_document = self.service.convert_schema_to_object(
            construction_document_deserialized,
            old_construction_document.idfilestorage
        )

        self.service.update_construction_document(construction_document)
        return {'id': id}

    @view_config(route_name='get_construction_documents_by_object', renderer='json')
    def get_construction_documents_by_object(self):
        object_id = int(self.request.matchdict['id'])
        construction_documents = self.service.get_construction_documents_by_object(object_id)
        documents = self.get_construction_documents_with_file_info(construction_documents)
        return documents

    @view_config(route_name='get_construction_documents_by_construction', renderer='json')
    def get_construction_documents_by_construction(self):
        construction_id = int(self.request.matchdict['id'])
        construction_documents = self.service.get_construction_documents_by_construction(construction_id)
        documents = self.get_construction_documents_with_file_info(construction_documents)
        return documents

    def get_construction_documents_with_file_info(self, construction_documents):
        documents = []
        for doc in construction_documents:
            file_info = self.service_filestorage.get_file_info_if_idfilestorage(doc.idfilestorage)
            documents.append(self.serializer.convert_object_to_json(doc, file_info))
        return documents
