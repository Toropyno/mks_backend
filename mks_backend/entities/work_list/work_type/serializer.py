from .model import WorkType

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class WorkTypeSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, work_type: WorkType) -> dict:
        return {
            'id': work_type.work_types_id,
            'fullName': work_type.fullname,
            'note': work_type.note
        }

    def to_mapped_object(self, schema: dict) -> WorkType:
        work_type = WorkType()

        work_type.work_types_id = schema.get('id')
        work_type.fullname = schema.get('fullName')
        work_type.note = schema.get('note')

        return work_type
