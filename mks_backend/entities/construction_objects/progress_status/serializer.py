from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler

from .model import ProgressStatus


class ProgressStatusSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, progress_status: ProgressStatus) -> dict:
        return {
            'id': progress_status.progress_statuses_id,
            'fullName': progress_status.fullname,
        }

    def to_mapped_object(self, schema: dict) -> ProgressStatus:
        progress_status = ProgressStatus()

        progress_status.progress_statuses_id = schema.get('id')
        progress_status.fullname = schema.get('fullName')

        return progress_status
