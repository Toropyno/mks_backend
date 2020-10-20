from typing import List

from mks_backend.models.inspections.inspection import Inspection
from mks_backend.serializers.utils.date_and_time import get_date_string

from mks_backend.errors.serilize_error import serialize_error_handler


class InspectionSerializer:

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

    def convert_list_to_json(self, inspections: List[Inspection]) -> list:
        return list(map(self.to_json, inspections))

    def convert_schema_to_object(self, schema: dict) -> Inspection:
        inspection = Inspection()

        inspection.inspections_id = schema.get('id')
        inspection.insp_date = schema.get('date')
        inspection.insp_name = schema.get('name')
        inspection.inspector = schema.get('inspector')
        inspection.insp_result = schema.get('result')

        return inspection
