import colander
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request

from mks_backend.services.construction_stage import ConstructionStageService
from mks_backend.serializers.construction_stage import ConstructionStageSerializer
from mks_backend.controllers.schemas.construction_stage import ConstructionStageSchema
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.errors.colavder_error import get_dictionary_with_errors_correct_format


class ConstructionStageController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionStageService()
        self.serializer = ConstructionStageSerializer()
        self.schema = ConstructionStageSchema()

    @view_config(route_name='construction_stages', request_method='GET', renderer='json')
    def get_all_construction_stages(self):
        construction_stages = self.service.get_all_construction_stages()
        return self.serializer.convert_list_to_json(construction_stages)

    @view_config(route_name='add_construction_stage', request_method='POST', renderer='json')
    def add_construction_stage(self):
        try:
            construction_stage_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_dictionary_with_errors_correct_format(error.asdict()))
        construction_stage = self.serializer.convert_schema_to_object(construction_stage_deserialized)
        try:
            self.service.add_construction_stage(construction_stage)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': construction_stage.construction_stages_id}

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_stage(self):
        id = int(self.request.matchdict['id'])
        construction_stage = self.service.get_construction_stage_by_id(id)
        return self.serializer.convert_object_to_json(construction_stage)

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_stage_by_id(id)
        return {'id': id}

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_stage(self):
        id = int(self.request.matchdict['id'])
        try:
            construction_stage_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_dictionary_with_errors_correct_format(error.asdict()))
        construction_stage_deserialized['id'] = id
        construction_stage = self.serializer.convert_schema_to_object(construction_stage_deserialized)
        try:
            self.service.update_construction_stage(construction_stage)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': id}
