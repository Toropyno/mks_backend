import colander
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from mks_backend.controllers.schemas.object_document import ObjectDocumentSchema
from mks_backend.errors.colander_error import get_collander_error_dict
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.object_document import ObjectDocumentSerializer
from mks_backend.services.object_document import ObjectDocumentService


class ObjectDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ObjectDocumentSerializer()
        self.service = ObjectDocumentService()
        self.schema = ObjectDocumentSchema()

    @view_config(route_name='object_documents', request_method='GET', renderer='json')
    def get_all_object_documents(self):
        object_documents = self.service.get_all_object_documents()
        return self.serializer.convert_list_to_json(object_documents)

    @view_config(route_name='add_object_document', request_method='POST', renderer='json')
    def add_object_document(self):
        try:
            object_document_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        object_document = self.serializer.convert_schema_to_object(object_document_deserialized)
        try:
            self.service.add_object_document(object_document)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': object_document.object_document_id}

    @view_config(route_name='object_document_delete_and_view', request_method='GET', renderer='json')
    def get_object_document(self):
        id = self.get_id_from_request()
        object_document = self.service.get_object_document_by_id(id)
        return self.serializer.convert_object_to_json(object_document)

    @view_config(route_name='object_document_delete_and_view', request_method='DELETE', renderer='json')
    def delete_object_document(self):
        id = self.get_id_from_request()
        self.service.delete_object_document_by_id(id)
        return {'id': id}

    def get_id_from_request(self):
        return int(self.request.matchdict['id'])
