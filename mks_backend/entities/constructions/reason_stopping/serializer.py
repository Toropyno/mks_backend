from .model import ReasonStopping

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class ReasonStoppingSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, reason_stopping: ReasonStopping) -> dict:
        return {
            'id': reason_stopping.reason_stopping_id,
            'fullName': reason_stopping.fullname,
        }

    def convert_schema_to_object(self, schema: dict) -> ReasonStopping:
        reason_stopping = ReasonStopping()

        reason_stopping.reason_stopping_id = schema.get('id')
        reason_stopping.fullname = schema.get('fullName')

        return reason_stopping
