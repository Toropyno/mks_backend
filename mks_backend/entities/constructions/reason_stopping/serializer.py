from .model import ReasonStopping

from mks_backend.errors import serialize_error_handler


class ReasonStoppingSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, reason_stopping: ReasonStopping) -> dict:
        return {
            'id': reason_stopping.reason_stopping_id,
            'fullName': reason_stopping.fullname,
        }

    def convert_list_to_json(self, reason_stoppings: list) -> list:
        return list(map(self.convert_object_to_json, reason_stoppings))

    def convert_schema_to_object(self, schema: dict) -> ReasonStopping:
        reason_stopping = ReasonStopping()

        reason_stopping.reason_stopping_id = schema.get('id')
        reason_stopping.fullname = schema.get('fullName')

        return reason_stopping
