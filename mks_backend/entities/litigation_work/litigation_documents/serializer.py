from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.documents.doc_type import DocTypeSerializer
from mks_backend.entities.filestorage import FileStorageSerializer
from mks_backend.utils.date_and_time import get_date_string, get_date_time_string

from .model import LitigationDocument


class LitigationDocumentSerializer(BaseSerializer):

    def to_json(self, litigation_document: LitigationDocument) -> dict:
        return {
            'id': litigation_document.litigation_documents_id,
            'litigationId': litigation_document.litigation_documents_id,
            'docType': DocTypeSerializer().to_json(litigation_document.doc_type),
            'docNumber': litigation_document.doc_number,
            'docDate': get_date_string(litigation_document.doc_date),
            'docName': litigation_document.doc_name,
            'note': litigation_document.note,
            'uploadDate': get_date_time_string(litigation_document.upload_date),
            'file': FileStorageSerializer.to_json(litigation_document.file_storage),
        }

    def to_mapped_object(self, schema_dict: dict) -> LitigationDocument:
        return LitigationDocument(
            litigation_documents_id=schema_dict.get('id'),
            idfilestorage=schema_dict.get('idFileStorage'),
            litigation_id=schema_dict.get('litigationId'),
            doctypes_id=schema_dict.get('docType'),
            doc_number=schema_dict.get('docNumber'),
            doc_date=schema_dict.get('docDate'),
            doc_name=schema_dict.get('docName'),
            note=schema_dict.get('note')
        )
