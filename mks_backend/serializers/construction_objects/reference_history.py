from mks_backend.models.construction_objects.reference_history import ReferenceHistory

from mks_backend.serializers.utils.date_and_time import get_date_string


class ReferenceHistorySerializer:

    def convert_list_to_json(self, reference_historys: list) -> list:
        return list(map(self.to_json, reference_historys))

    def to_json(self, reference_history: ReferenceHistory) -> dict:
        return {
            'id': reference_history.references_history_id,
            'constructionObjectId': reference_history.construction_objects_id,
            'endDate': get_date_string(reference_history.end_date),
            'constructionCode': reference_history.construction.project_code,
            'constructionName': reference_history.construction.project_name,
        }
