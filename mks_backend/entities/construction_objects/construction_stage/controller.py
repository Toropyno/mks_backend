from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ConstructionStageSchema
from .serializer import ConstructionStageSerializer
from .service import ConstructionStageService


@view_defaults(renderer='json')
class ConstructionStageController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionStageService()
        self.serializer = ConstructionStageSerializer()
        self.schema = ConstructionStageSchema()

    @view_config(route_name='get_all_construction_stages')
    def get_all_construction_stages(self):
        construction_stages = self.service.get_all_construction_stages()
        return self.serializer.convert_list_to_json(construction_stages)

    @view_config(route_name='add_construction_stage')
    def add_construction_stage(self):
        construction_stage_deserialized = self.schema.deserialize(self.request.json_body)
        construction_stage = self.serializer.convert_schema_to_object(construction_stage_deserialized)

        self.service.add_construction_stage(construction_stage)
        return {'id': construction_stage.construction_stages_id}

    @view_config(route_name='get_construction_stage')
    def get_construction_stage(self):
        id_ = int(self.request.matchdict['id'])
        construction_stage = self.service.get_construction_stage_by_id(id_)
        return self.serializer.convert_object_to_json(construction_stage)

    @view_config(route_name='delete_construction_stage')
    def delete_construction_object(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_stage_by_id(id_)
        return {'id': id_}

    @view_config(route_name='edit_construction_stage')
    def edit_construction_stage(self):
        construction_stage_deserialized = self.schema.deserialize(self.request.json_body)
        construction_stage_deserialized['id'] = int(self.request.matchdict['id'])

        construction_stage = self.serializer.convert_schema_to_object(construction_stage_deserialized)
        self.service.update_construction_stage(construction_stage)
        return {'id': construction_stage.construction_stages_id}
