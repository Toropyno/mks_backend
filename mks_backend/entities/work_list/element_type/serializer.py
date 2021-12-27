from .model import ElementType

from mks_backend.entities.BASE.serializer import BaseSerializer


class ElementTypeSerializer(BaseSerializer):

    @classmethod
    def to_json(cls, element_type: ElementType) -> dict:
        return {
            'id': element_type.element_types_id,
            'fullName': element_type.fullname,
        }

    def convert_schema_to_object(self, schema: dict) -> ElementType:
        element_type = ElementType()

        element_type.element_types_id = schema.get('id')
        element_type.fullname = schema.get('fullName')

        return element_type
