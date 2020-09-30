from mks_backend.models.documents.object_document import ObjectDocument


class ObjectDocumentSerializer:

    def convert_object_to_json(self, object_document: ObjectDocument) -> dict:
        return {
            'id': object_document.object_documents_id,
            'constructionObjectId': object_document.construction_objects_id,
            'constructionDocumentId': object_document.construction_documents_id
        }

    def convert_list_to_json(self, object_document_list: list) -> list:
        return list(map(self.convert_object_to_json, object_document_list))
