from .model import DocType


class DocTypeSerializer:

    def convert_object_to_json(self, doc_type: DocType) -> dict:
        return {
            'id': doc_type.doctypes_id,
            'code': doc_type.code,
            'fullName': doc_type.fullname
        }

    def convert_list_to_json(self, doc_type_list: list) -> list:
        return list(map(self.convert_object_to_json, doc_type_list))

    def convert_schema_to_object(self, schema: dict) -> DocType:
        doc_types = DocType()

        doc_types.doctypes_id = schema.get('id')
        doc_types.code = schema.get('code')
        doc_types.fullname = schema.get('fullName')

        return doc_types
