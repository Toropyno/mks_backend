from .model import ConstructionType

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class ConstructionTypeSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, construction_type: ConstructionType) -> dict:
        return {
            'id': construction_type.construction_types_id,
            'fullName': construction_type.fullname
        }

    def to_mapped_object(self, schema: dict) -> ConstructionType:
        construction_type = ConstructionType()

        construction_type.construction_types_id = schema.get('id')
        construction_type.fullname = schema.get('fullName')

        return construction_type
