from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.construction_progress import ConstructionProgress
from mks_backend.serializers._date_utils import get_date_string, get_date_time_string


class ConstructionProgressSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_progress: ConstructionProgress) -> dict:
        construction_progress_dict = {
            'id': construction_progress.construction_progress_id,
            'constructionObjectsId': construction_progress.construction_objects_id,
            'reportingDate': get_date_string(construction_progress.reporting_date),
            'readiness': construction_progress.readiness,
            'people': construction_progress.people,
            'equipment': construction_progress.equipment,
            # 'progressStatusesId': construction_progress.progress_statuses_id,
            'updateDatetime': get_date_time_string(construction_progress.update_datetime),
        }
        return construction_progress_dict

    def convert_list_to_json(self, construction_progresses_list: list) -> list:
        return list(map(self.convert_object_to_json, construction_progresses_list))

    def convert_schema_to_object(self, schema: dict) -> ConstructionProgress:
        construction_progress = ConstructionProgress()
        if 'id' in schema:
            construction_progress.construction_progress_id = schema['id']

        construction_progress.construction_objects_id = schema['constructionObjectsId']
        construction_progress.reporting_date = schema['reportingDate']
        construction_progress.readiness = schema['readiness']
        construction_progress.people = schema['people']
        construction_progress.equipment = schema['equipment']
        construction_progress.progress_statuses_id = schema['progressStatusesId']
        construction_progress.update_datetime = schema['updateDatetime']

        return construction_progress
