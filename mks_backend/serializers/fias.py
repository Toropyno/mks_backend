from mks_backend.models.fias import FIAS


class FIASSerializer:

    def convert_schema_to_object(self, schema: dict) -> FIAS:
        fias = FIAS()

        fias.subject = schema.get('subject')
        fias.district = schema.get('district')
        fias.city = schema.get('city')
        fias.locality = schema.get('locality')
        fias.remaining_address = schema.get('remainingAddress')

        return fias
