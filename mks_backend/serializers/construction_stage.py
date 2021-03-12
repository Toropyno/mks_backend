from mks_backend.models.construction_stage import ConstructionStage

from mks_backend.errors import serialize_error_handler


class ConstructionStageSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_stage: ConstructionStage) -> dict:
        return {
            'id': construction_stage.construction_stages_id,
            'code': construction_stage.code,
            'fullName': construction_stage.fullname,
            'hierarchyLevel': construction_stage.hierarchy_level,
            'parent': {
                'id': construction_stage.parent.construction_stages_id,
                'fullName': construction_stage.parent.fullname,
            } if construction_stage.parent else None
        }

    def convert_list_to_json(self, construction_stages: list) -> list:
        return list(map(self.convert_object_to_json, construction_stages))

    def convert_schema_to_object(self, schema: dict) -> ConstructionStage:
        construction_stage = ConstructionStage()
        if 'id' in schema:
            construction_stage.construction_stages_id = schema['id']

        construction_stage.code = schema.get('code')
        construction_stage.fullname = schema.get('fullName')
        construction_stage.hierarchy_level = schema.get('hierarchyLevel')
        construction_stage.ref_construction_stages_id = schema.get('parent')
        return construction_stage
