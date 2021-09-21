from .model import ElementType


class ElementTypeSerializer:

    @classmethod
    def convert_object_to_json(cls, element_type: ElementType) -> dict:
        return {
            'id': element_type.element_types_id,
            'fullName': element_type.fullname,
        }

    def convert_list_to_json(self, element_types: list) -> list:
        return list(map(self.convert_object_to_json, element_types))

    def convert_schema_to_object(self, schema: dict) -> ElementType:
        element_type = ElementType()

        element_type.element_types_id = schema.get('id')
        element_type.fullname = schema.get('fullName')

        return element_type
