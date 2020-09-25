from mks_backend.models.work_type import WorkType

from mks_backend.errors.serilize_error import serialize_error_handler


class WorkTypeSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, work_type: WorkType) -> dict:
        return {
            'id': work_type.work_types_id,
            'fullName': work_type.fullname,
            'note': work_type.note
        }

    def convert_list_to_json(self, work_types: list) -> list:
        return list(map(self.convert_object_to_json, work_types))

    def convert_schema_to_object(self, schema: dict) -> WorkType:
        work_type = WorkType()

        work_type.work_types_id = schema.get('id')
        work_type.fullname = schema.get('fullName')
        work_type.note = schema.get('note')

        return work_type
