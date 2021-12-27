from .model import Inspection

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.utils.date_and_time import get_date_string
from mks_backend.errors import serialize_error_handler


class InspectionSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, inspection: Inspection) -> dict:
        return {
            'id': inspection.inspections_id,
            'date': get_date_string(inspection.insp_date),
            'name': inspection.insp_name,
            'inspector': inspection.inspector,
            'result': inspection.insp_result,
        }

    def convert_schema_to_object(self, schema: dict) -> Inspection:
        inspection = Inspection()

        inspection.inspections_id = schema.get('id')
        inspection.insp_date = schema.get('date')
        inspection.insp_name = schema.get('name')
        inspection.inspector = schema.get('inspector')
        inspection.insp_result = schema.get('result')

        return inspection
