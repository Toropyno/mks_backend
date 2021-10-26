from .model import Courts

from mks_backend.errors import serialize_error_handler


class CourtSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, courts: Courts) -> dict:
        return {
            'id': courts.courts_id,
            'fullName': courts.fullname,
        }

    def convert_list_to_json(self, courts: list) -> list:
        return list(map(self.convert_object_to_json, courts))

    def convert_schema_to_object(self, schema: dict) -> Courts:
        courts = Courts()

        courts.courts_id = schema.get('id')
        courts.fullname = schema.get('fullName')

        return courts
