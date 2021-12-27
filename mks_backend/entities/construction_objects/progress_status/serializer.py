from .model import ProgressStatus

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class ProgressStatusSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, progress_status: ProgressStatus) -> dict:
        return {
            'id': progress_status.progress_statuses_id,
            'fullName': progress_status.fullname,
        }

    def convert_schema_to_object(self, schema: dict) -> ProgressStatus:
        progress_status = ProgressStatus()

        progress_status.progress_statuses_id = schema.get('id')
        progress_status.fullname = schema.get('fullName')

        return progress_status
