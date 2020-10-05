from mks_backend.models.construction_progress import ConstructionProgress
from mks_backend.serializers.utils.date_and_time import get_date_string, get_date_time_string
from datetime import datetime

from mks_backend.errors.serilize_error import serialize_error_handler


class ConstructionProgressSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_progress: ConstructionProgress) -> dict:
        readiness = float(construction_progress.readiness) if construction_progress.readiness else None

        return {
            'id': construction_progress.construction_progress_id,
            'constructionObjects': construction_progress.construction_objects_id,
            'reportingDate': get_date_string(construction_progress.reporting_date),
            'readiness': readiness,
            'people': construction_progress.people,
            'equipment': construction_progress.equipment,
            'progressStatuses': construction_progress.progress_statuses_id,
            'updateDatetime': get_date_time_string(construction_progress.update_datetime),
        }

    def convert_list_to_json(self, construction_progresses_list: list) -> list:
        return list(map(self.convert_object_to_json, construction_progresses_list))

    def convert_schema_to_object(self, schema: dict) -> ConstructionProgress:
        construction_progress = ConstructionProgress()

        construction_progress.construction_progress_id = schema.get('id')
        construction_progress.construction_objects_id = schema.get('constructionObjects')
        construction_progress.reporting_date = schema.get('reportingDate')
        construction_progress.readiness = schema.get('readiness')
        construction_progress.people = schema.get('people')
        construction_progress.equipment = schema.get('equipment')
        construction_progress.progress_statuses_id = schema.get('progressStatuses')

        construction_progress.update_datetime = datetime.now()
        return construction_progress
