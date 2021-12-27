from .model import ObjectCompletion

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.utils.date_and_time import get_date_string, get_date_time_string


class ObjectCompletionSerializer(BaseSerializer):

    def to_json(self, object_completion: ObjectCompletion) -> dict:
        return {
            'id': object_completion.object_completion_id,
            'plannedDate': get_date_string(object_completion.planned_date),
            'updateDatetime': get_date_time_string(object_completion.update_datetime),
        }
