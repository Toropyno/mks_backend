from .model import RealtyType

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class RealtyTypeSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, realty_type: RealtyType) -> dict:
        return {
            'id': realty_type.realty_types_id,
            'fullName': realty_type.fullname
        }

    def to_mapped_object(self, schema: dict) -> RealtyType:
        realty_type = RealtyType()

        realty_type.realty_types_id = schema.get('id')
        realty_type.fullname = schema.get('fullName')

        return realty_type
