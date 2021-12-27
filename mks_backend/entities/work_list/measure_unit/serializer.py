from .model import MeasureUnit

from mks_backend.entities.BASE.serializer import BaseSerializer


class MeasureUnitSerializer(BaseSerializer):

    @classmethod
    def to_json(cls, measure_unit: MeasureUnit) -> dict:
        return {
            'id': measure_unit.unit_id,
            'code': measure_unit.unit_code,
            'name': measure_unit.unit_name
        }

    def convert_schema_to_object(self, schema: dict) -> MeasureUnit:
        measure_unit = MeasureUnit()

        measure_unit.unit_id = schema.get('id')
        measure_unit.unit_code = schema.get('code')
        measure_unit.unit_name = schema.get('name')

        return measure_unit
