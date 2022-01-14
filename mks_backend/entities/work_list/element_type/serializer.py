from mks_backend.entities.BASE.serializer import BaseSerializer

from .model import ElementType


class ElementTypeSerializer(BaseSerializer):

    @classmethod
    def to_json(cls, element_type: ElementType) -> dict:
        return {
            'id': element_type.element_types_id,
            'fullName': element_type.fullname,
        }

    def to_mapped_object(self, schema: dict) -> ElementType:
        element_type = ElementType()

        element_type.element_types_id = schema.get('id')
        element_type.fullname = schema.get('fullName')

        return element_type
