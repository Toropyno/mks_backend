from mks_backend.models.work_list.measure_unit import MeasureUnit


class MeasureUnitSerializer:

    @classmethod
    def convert_object_to_json(cls, measure_unit: MeasureUnit) -> dict:
        return {
            'id': measure_unit.unit_id,
            'code': measure_unit.unit_code,
            'fullName': measure_unit.unit_name
        }

    def convert_list_to_json(self, measure_unit_list: list) -> list:
        return list(map(self.convert_object_to_json, measure_unit_list))

    def convert_schema_to_object(self, schema: dict) -> MeasureUnit:
        measure_unit = MeasureUnit()

        measure_unit.unit_id = schema.get('id')
        measure_unit.unit_code = schema.get('code')
        measure_unit.unit_name = schema.get('name')

        return measure_unit
