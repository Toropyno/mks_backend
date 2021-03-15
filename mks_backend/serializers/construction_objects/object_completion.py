from mks_backend.models.construction_objects.object_completion import ObjectCompletion

from mks_backend.serializers.utils.date_and_time import get_date_string, get_date_time_string


class ObjectCompletionSerializer:

    def convert_list_to_json(self, object_completions: list) -> list:
        return list(map(self.to_json, object_completions))

    def to_json(self, object_completion: ObjectCompletion) -> dict:
        return {
            'id': object_completion.object_completion_id,
            'plannedDate': get_date_string(object_completion.planned_date),
            'updateDatetime': get_date_time_string(object_completion.update_datetime),
        }
