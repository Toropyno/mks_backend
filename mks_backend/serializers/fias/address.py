from mks_backend.errors.serilize_error import serialize_error_handler


class FIASAPISerializer:

    @serialize_error_handler
    def convert_full_fias(self, schema: dict) -> str:
        return schema.get('fullFias').replace('/', ' ')
