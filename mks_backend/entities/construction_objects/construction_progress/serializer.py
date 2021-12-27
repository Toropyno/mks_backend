from datetime import datetime

from .model import ConstructionProgress

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.construction_objects.progress_status import ProgressStatusSerializer
from mks_backend.utils.date_and_time import get_date_string, get_date_time_string
from mks_backend.errors import serialize_error_handler


class ConstructionProgressSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, construction_progress: ConstructionProgress) -> dict:
        return {
            'id': construction_progress.construction_progress_id,
            'constructionObjects': construction_progress.construction_objects_id,
            'reportingDate': get_date_string(construction_progress.reporting_date),
            'readiness': format(construction_progress.readiness, '.2f'),
            'people': construction_progress.people,
            'equipment': construction_progress.equipment,
            'peoplePlan': construction_progress.people_plan,
            'equipmentPlan': construction_progress.equipment_plan,
            'progressStatus': ProgressStatusSerializer.to_json(construction_progress.progress_status),
            'updateDatetime': get_date_time_string(construction_progress.update_datetime),

        }

    def convert_schema_to_object(self, schema: dict) -> ConstructionProgress:
        construction_progress = ConstructionProgress()

        construction_progress.construction_progress_id = schema.get('id')
        construction_progress.construction_objects_id = schema.get('constructionObjects')
        construction_progress.reporting_date = schema.get('reportingDate')
        construction_progress.readiness = schema.get('readiness')
        construction_progress.people = schema.get('people')
        construction_progress.equipment_plan = schema.get('equipmentPlan')
        construction_progress.people_plan = schema.get('peoplePlan')
        construction_progress.equipment = schema.get('equipment')
        construction_progress.progress_statuses_id = schema.get('progressStatus')

        construction_progress.update_datetime = datetime.now()
        return construction_progress
