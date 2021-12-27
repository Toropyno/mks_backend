from .model import Courts

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class CourtSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, courts: Courts) -> dict:
        return {
            'id': courts.courts_id,
            'fullName': courts.fullname,
        }

    def to_mapped_object(self, schema: dict) -> Courts:
        courts = Courts()

        courts.courts_id = schema.get('id')
        courts.fullname = schema.get('fullName')

        return courts
