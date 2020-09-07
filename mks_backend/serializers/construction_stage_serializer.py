from mks_backend.models.construction_stages import ConstructionStages

from mks_backend.errors.serilize_error import serialize_error_handler


class ConstructionStageSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_stage: ConstructionStages) -> dict:
        construction_stage_dict = {
            'id': construction_stage.construction_stages_id,
            'code': construction_stage.code,
            'fullName': construction_stage.fullname,
        }
        return construction_stage_dict

    def convert_list_to_json(self, construction_stages: list) -> list:
        return list(map(self.convert_object_to_json, construction_stages))

    def convert_schema_to_object(self, schema: dict) -> ConstructionStages:
        construction_stage = ConstructionStages()
        if 'id' in schema:
            construction_stage.construction_stages_id = schema['id']

        construction_stage.code = schema['code']
        construction_stage.fullname = schema['fullName']
        return construction_stage
