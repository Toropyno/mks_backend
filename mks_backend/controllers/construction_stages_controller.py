import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.services.construction_stage_service import ConstructionStageService
from mks_backend.serializers.construction_stage_serializer import ConstructionStageSerializer
from mks_backend.controllers.schemas.construction_stages_schema import ConstructionStagesSchema

class ConstructionStagesController(object):

    def __init__(self, request):
        self.request = request
        self.service = ConstructionStageService()
        self.serializer = ConstructionStageSerializer()

    @view_config(route_name='construction_stages', request_method='GET', renderer='json')
    def get_all_construction_stages(self):
        construction_stages = self.service.get_all_construction_stages()
        json = self.serializer.convert_list_to_json(construction_stages)
        return json

    @view_config(route_name='add_construction_stage', request_method='POST', renderer='json')
    def add_construction_stage(self):
        construction_stage_schema = ConstructionStagesSchema()
        try:
            construction_stage_deserialized = construction_stage_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        construction_stage = self.serializer.convert_schema_to_object(construction_stage_deserialized)
        self.service.add_construction_stage(construction_stage)
        return {'id': construction_stage.construction_stages_id}

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_stage(self):
        id = self.request.matchdict['id']
        construction_stage = self.service.get_construction_stage_by_id(id)
        json = self.serializer.convert_object_to_json(construction_stage)
        return json

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        id = self.request.matchdict['id']
        self.service.delete_construction_stage_by_id(id)
        return {'id': id}

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_stage(self):
        id = self.request.matchdict['id']
        construction_stage_schema = ConstructionStagesSchema()
        try:
           construction_stage_deserialized = construction_stage_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
           return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
           return Response(status=403, json_body=date_parse_error.args)
        construction_stage_deserialized["id"] = id
        construction_stage = self.serializer.convert_schema_to_object(construction_stage_deserialized)
        self.service.update_construction_stage(construction_stage)
        return {'id': id}
