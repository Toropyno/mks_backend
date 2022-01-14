from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.documents.doc_type import DocTypeSerializer
from mks_backend.entities.filestorage import FileStorageSerializer
from mks_backend.utils.date_and_time import get_date_string, get_date_time_string

from .model import ConstructionDocument


class ConstructionDocumentSerializer(BaseSerializer):

    def to_json(self, construction_document: ConstructionDocument) -> dict:
        return {
            'id': construction_document.construction_documents_id,
            'constructionId': construction_document.construction_id,
            'docType': DocTypeSerializer().to_json(construction_document.doc_type),
            'validUntil': get_date_string(construction_document.valid_until),
            'docNumber': construction_document.doc_number,
            'docDate': get_date_string(construction_document.doc_date),
            'docName': construction_document.doc_name,
            'note': construction_document.note,
            'uploadDate': get_date_time_string(construction_document.upload_date),
            'file': FileStorageSerializer.to_json(construction_document.file_storage),
        }
