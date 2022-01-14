from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler

from .model import ConstructionStage


class ConstructionStageSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, construction_stage: ConstructionStage) -> dict:
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

    def to_mapped_object(self, schema: dict) -> ConstructionStage:
        construction_stage = ConstructionStage()
        if 'id' in schema:
            construction_stage.construction_stages_id = schema['id']

        construction_stage.code = schema.get('code')
        construction_stage.fullname = schema.get('fullName')
        construction_stage.hierarchy_level = schema.get('hierarchyLevel')
        construction_stage.ref_construction_stages_id = schema.get('parent')
        return construction_stage
