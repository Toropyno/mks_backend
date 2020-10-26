from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.fias import FIAS


class FIASSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, fias: FIAS) -> dict:
        return {
            'id': fias.id,
            'subject': fias.subject,
            'district': fias.district,
            'city': fias.city,
            'locality': fias.locality,
            'remainingAddress': fias.remaining_address,
            'aoid': fias.aoid
        }

    def convert_list_to_json(self, fiases: list) -> list:
        return list(map(self.convert_object_to_json, fiases))

    def convert_schema_to_object(self, schema: dict) -> FIAS:
        fias = FIAS()

        fias.id = schema.get('id')
        fias.subject = schema.get('subject')
        fias.district = schema.get('district')
        fias.city = schema.get('city')
        fias.locality = schema.get('locality')
        fias.remaining_address = schema.get('remainingAddress')

        return fias

    def convert_full_fias(self, schema: dict) -> str:
        return schema.get('fullFias').replace('/', ' ')
