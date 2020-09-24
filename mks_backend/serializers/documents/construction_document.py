from datetime import datetime

from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.serializers.utils.date_and_time import get_date_string, get_date_time_string


class ConstructionDocumentSerializer:

    def convert_object_to_json(self, construction_document: ConstructionDocument) -> dict:
        return {
            'id': construction_document.construction_documents_id,
            'constructionId': construction_document.construction_id,
            # 'docTypesId': construction_document.doctypes_id,
            'docNumber': construction_document.doc_number,
            'docDate': get_date_string(construction_document.doc_date),
            'docName': construction_document.doc_name,
            'note': construction_document.note,
            'idFileStorage': construction_document.idfilestorage,
            'uploadDate': get_date_time_string(construction_document.upload_date),
        }

    def convert_list_to_json(self, construction_document_documents: list) -> list:
        return list(map(self.convert_object_to_json, construction_document_documents))

    def convert_schema_to_object(self, schema_dict: dict) -> ConstructionDocument:
        construction_document = ConstructionDocument()

        construction_document.construction_documents_id = schema_dict.get('id')
        construction_document.construction_id = schema_dict.get('constructionId')
        # construction_document.doctypes_id = schema_dict.get('docTypesId')
        construction_document.doc_number = schema_dict.get('docNumber')
        construction_document.doc_date = schema_dict.get('docDate')
        construction_document.doc_name = schema_dict.get('docName')
        construction_document.note = schema_dict.get('note')
        construction_document.idfilestorage = schema_dict.get('idFileStorage')

        construction_document.upload_date = datetime.now()
        return construction_document
