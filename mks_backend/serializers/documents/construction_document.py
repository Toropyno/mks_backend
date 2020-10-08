from datetime import datetime

from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.serializers.documents.doc_type import DocTypeSerializer
from mks_backend.serializers.filestorage import FileStorageSerializer
from mks_backend.serializers.utils.date_and_time import get_date_string, get_date_time_string


class ConstructionDocumentSerializer:

    def convert_object_to_json(self, construction_document: ConstructionDocument, file_info=None) -> dict:
        upload_date = None
        if construction_document.idfilestorage:
            file_info = FileStorageSerializer.convert_file_info_with_idfilestorage(
                construction_document.idfilestorage,
                file_info,
            )
            upload_date = self.get_upload_date(construction_document.upload_date)

        return {
            'id': construction_document.construction_documents_id,
            'constructionId': construction_document.construction_id,
            'docType': DocTypeSerializer().convert_object_to_json(construction_document.doc_type),
            'docNumber': construction_document.doc_number,
            'docDate': get_date_string(construction_document.doc_date),
            'docName': construction_document.doc_name,
            'note': construction_document.note,
            'uploadDate': upload_date,
            'file': file_info,
        }

    def convert_list_to_json(self, construction_documents: list) -> list:
        return list(map(self.convert_object_to_json, construction_documents))

    def get_upload_date(self, upload_date: datetime) -> str:
        if upload_date:
            return get_date_time_string(upload_date)
