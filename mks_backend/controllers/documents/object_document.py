from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.serializers.documents.object_document import ObjectDocumentSerializer
from mks_backend.services.documents.object_document import ObjectDocumentService


class ObjectDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ObjectDocumentSerializer()
        self.service = ObjectDocumentService()

    @view_config(route_name='get_all_object_documents', request_method='GET', renderer='json')
    def get_all_object_documents(self):
        object_documents = self.service.get_all_object_documents()
        return self.serializer.convert_list_to_json(object_documents)
