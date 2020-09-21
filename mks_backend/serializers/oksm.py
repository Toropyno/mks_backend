from mks_backend.models.oksm import OKSM

from mks_backend.errors.serilize_error import serialize_error_handler


class OKSMSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, oksm: OKSM) -> dict:
        return {
            'id': oksm.oksm_id,
            'code': oksm.code,
            'shortName': oksm.shortname,
            'fullName': oksm.fullname,
            'alpha2': oksm.alpha2,
            'alpha3': oksm.alpha3,
        }

    def convert_list_to_json(self, oksms: list) -> list:
        return list(map(self.convert_object_to_json, oksms))

    def convert_schema_to_object(self, schema: dict) -> OKSM:
        oksm = OKSM()

        oksm.construction_companies_id = schema.get('id')
        oksm.code = schema.get('code')
        oksm.shortname = schema.get('shortName')
        oksm.fullname = schema.get('fullName')
        oksm.alpha2 = schema.get('alpha2')
        oksm.alpha3 = schema.get('alpha3')

        return oksm
