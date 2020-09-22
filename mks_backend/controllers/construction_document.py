import colander
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.controllers.schemas.construction_document import ConstructionDocumentSchema
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.construction_document import ConstructionDocumentSerializer
from mks_backend.services.construction_document import ConstructionDocumentService
from mks_backend.errors.colander_error import get_collander_error_dict


class ConstructionDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionDocumentSerializer()
        self.service = ConstructionDocumentService()
        self.schema = ConstructionDocumentSchema()

    @view_config(route_name='get_all_construction_documents', renderer='json')
    def get_all_construction_documents(self):
        construction_documents = self.service.get_all_construction_documents()
        return self.serializer.convert_list_to_json(construction_documents)

    @view_config(route_name='add_construction_document', renderer='json')
    def add_construction_document(self):
        try:
            construction_document_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        construction_document = self.serializer.convert_schema_to_object(construction_document_deserialized)
        try:
            self.service.add_construction_document(construction_document)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': construction_document.construction_documents_id}

    @view_config(route_name='get_construction_document', renderer='json')
    def get_construction_document(self):
        id = int(self.request.matchdict['id'])
        construction_document = self.service.get_construction_document_by_id(id)
        return self.serializer.convert_object_to_json(construction_document)

    @view_config(route_name='delete_construction_document', renderer='json')
    def delete_construction_document(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_document_by_id_with_filestorage_cascade(id)
        return {'id': id}

    @view_config(route_name='edit_construction_document', renderer='json')
    def edit_construction_document(self):
        id = int(self.request.matchdict['id'])
        try:
            construction_document_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        construction_document_deserialized['id'] = id
        construction_document = self.serializer.convert_schema_to_object(construction_document_deserialized)
        try:
            self.service.update_construction_document(construction_document)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': id}
