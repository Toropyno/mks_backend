from mks_backend.models.fias.fias import FIAS


class FIASSerializer:

    def convert_schema_to_subject(self, schema: dict) -> FIAS:
        fias = FIAS()

        fias.subject = schema.get('subject')
        fias.district = schema.get('district')

        return fias
