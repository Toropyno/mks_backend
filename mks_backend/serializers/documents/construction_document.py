from datetime import datetime

from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.serializers.documents.doc_type import DocTypeSerializer
from mks_backend.serializers.filestorage import FileStorageSerializer
from mks_backend.serializers.utils.date_and_time import get_date_string, get_date_time_string


class ConstructionDocumentSerializer:

    def convert_object_to_json(self, construction_document: ConstructionDocument) -> dict:
        return {
            'id': construction_document.construction_documents_id,
            'constructionId': construction_document.construction_id,
            'docType': DocTypeSerializer().convert_object_to_json(construction_document.doc_type),
            'docNumber': construction_document.doc_number,
            'docDate': get_date_string(construction_document.doc_date),
            'docName': construction_document.doc_name,
            'note': construction_document.note,
            'uploadDate': get_date_time_string(construction_document.upload_date),
            'file': FileStorageSerializer.to_json(
                construction_document.file_storage
            ),
        }

    def convert_list_to_json(self, construction_documents: list) -> list:
        return list(map(self.convert_object_to_json, construction_documents))
