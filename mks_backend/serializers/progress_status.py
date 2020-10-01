from mks_backend.models.progress_status import ProgressStatus

from mks_backend.errors.serilize_error import serialize_error_handler


class ProgressStatusSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, progress_status: ProgressStatus) -> dict:
        return {
            'id': progress_status.progress_statuses_id,
            'code': progress_status.fullname,
        }

    def convert_list_to_json(self, progress_statuses: list) -> list:
        return list(map(self.convert_object_to_json, progress_statuses))

    def convert_schema_to_object(self, schema: dict) -> ProgressStatus:
        progress_status = ProgressStatus()

        progress_status.progress_statuses_id = schema.get('id')
        progress_status.fullname = schema.get('fullName')

        return progress_status
