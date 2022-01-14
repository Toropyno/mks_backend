from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler

from .model import OKSM


class OKSMSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, oksm: OKSM) -> dict:
        return {
            'id': oksm.oksm_id,
            'code': oksm.code,
            'shortName': oksm.shortname,
            'fullName': oksm.fullname,
            'alpha2': oksm.alpha2,
            'alpha3': oksm.alpha3,
        }

    def to_mapped_object(self, schema: dict) -> OKSM:
        oksm = OKSM()

        oksm.oksm_id = schema.get('id')
        oksm.code = schema.get('code')
        oksm.shortname = schema.get('shortName')
        oksm.fullname = schema.get('fullName')
        oksm.alpha2 = schema.get('alpha2')
        oksm.alpha3 = schema.get('alpha3')

        return oksm
