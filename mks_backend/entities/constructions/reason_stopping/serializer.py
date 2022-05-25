from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler

from .model import ReasonStopping


class ReasonStoppingSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, reason_stopping: ReasonStopping) -> dict:
        return {
            'id': reason_stopping.reasons_stopping_id,
            'fullName': reason_stopping.fullname,
        }

    def to_mapped_object(self, schema: dict) -> ReasonStopping:
        reason_stopping = ReasonStopping()

        reason_stopping.reason_stopping_id = schema.get('id')
        reason_stopping.fullname = schema.get('fullName')

        return reason_stopping
