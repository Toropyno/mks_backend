from .model import ReferenceHistory

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.utils.date_and_time import get_date_string


class ReferenceHistorySerializer(BaseSerializer):

    def to_json(self, reference_history: ReferenceHistory) -> dict:
        return {
            'id': reference_history.references_history_id,
            'constructionObjectId': reference_history.construction_objects_id,
            'endDate': get_date_string(reference_history.end_date),
            'constructionCode': reference_history.construction.project_code,
            'constructionName': reference_history.construction.project_name,
        }
