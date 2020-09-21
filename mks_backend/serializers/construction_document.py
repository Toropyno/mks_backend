from datetime import date as Date
from datetime import datetime as DateTime

from mks_backend.models.construction_document import ConstructionDocument


class ConstructionDocumentSerializer:

    def convert_object_to_json(self, construction_document: ConstructionDocument) -> dict:
        return {
            'id': construction_document.construction_documents_id,
            'constructionId': construction_document.construction_id,
            'docTypesId': construction_document.doctypes_id,
            'docNumber': construction_document.doc_number,
            'docDate': self.get_date_string(construction_document.doc_date),
            'docName': construction_document.doc_name,
            'note': construction_document.note,
            'idFileStorage': construction_document.idfilestorage,
            'uploadDate': self.get_date_time_string(construction_document.upload_date),
        }

    def convert_list_to_json(self, construction_document_documents: list) -> list:
        return list(map(self.convert_object_to_json, construction_document_documents))

    def convert_schema_to_object(self, schema_dict: dict) -> ConstructionDocument:
        construction_document = ConstructionDocument()
        construction_document.construction_documents_id = schema_dict['id']
        construction_document.construction_id = schema_dict['constructionId']
        construction_document.doctypes_id = schema_dict['docTypesId']
        construction_document.doc_number = schema_dict['docNumber']
        construction_document.doc_date = schema_dict['docDate']
        construction_document.doc_name = schema_dict['docName']
        construction_document.note = schema_dict['note']
        construction_document.idfilestorage = schema_dict['idFileStorage']
        construction_document.upload_date = schema_dict['uploadDate']
        return construction_document

    def get_date_string(self, date: Date) -> str:
        return str(date.year) + ',' + str(date.month) + ',' + str(date.day)

    def get_date_time_string(self, date_time: DateTime) -> str:
        return str(date_time.year) + ',' + str(date_time.month) + ',' + str(date_time.day) + \
               ' ' + str(date_time.hour) + ':' + str(date_time.minute) + ':' + str(date_time.second)