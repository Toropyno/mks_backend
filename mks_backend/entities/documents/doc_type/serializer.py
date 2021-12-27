from .model import DocType

from mks_backend.entities.BASE.serializer import BaseSerializer


class DocTypeSerializer(BaseSerializer):

    def to_json(self, doc_type: DocType) -> dict:
        return {
            'id': doc_type.doctypes_id,
            'code': doc_type.code,
            'fullName': doc_type.fullname
        }

    def to_mapped_object(self, schema: dict) -> DocType:
        doc_types = DocType()

        doc_types.doctypes_id = schema.get('id')
        doc_types.code = schema.get('code')
        doc_types.fullname = schema.get('fullName')

        return doc_types
