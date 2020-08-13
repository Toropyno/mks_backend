import colander
from pyramid.view import view_config
from pyramid.response import Response

#from mks_backend.services.construction_stages_service import ConstructionStagesService
#from mks_backend.serializers.construction_stages_serializer import ConstructionStagesSerializer



class ConstructionStagesController(object):

    def __init__(self, request):
        self.request = request
        self.service = None #ConstructionStagesService()
        self.serializer = None #ConstructionStagesSerializer()

    @view_config(route_name='construction_stages', request_method='GET', renderer='json')
    def get_all_construction_stages(self):
        pass
        #construction_stages_array = self.service.get_all_construction_stages()
        #json = self.serializer.convert_list_to_json(construction_stages_array)
        #return json

    @view_config(route_name='add_construction_stage', request_method='POST', renderer='json')
    def add_construction_stage(self):
        pass
        ##construction_stage_schema = ConstructionStagetControllerSchema()
        ##try:
        ##    construction_stage_deserialized = construction_stage_schema.deserialize(self.request.json_body)
        ##except colander.Invalid as error:
        ##    return Response(status=403, json_body=error.asdict())
        ##except ValueError as date_parse_error:
        ##    return Response(status=403, json_body=date_parse_error.args)
        #construction_stage = self.service.get_object(self.request.json_body)#convert_schema_to_object(construction_stage_deserialized)
        #self.service.add_construction_stage(construction_stage)
        #return {'id': construction_stage.construction_stage_id}

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_stage(self):
        pass
        #id = self.request.matchdict['id']
        #construction_stage = self.service.get_construction_stage_by_id(id)
        #json = self.serializer.convert_object_to_json(construction_stage)
        #return json

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        pass
        #id = self.request.matchdict['id']
        #self.service.delete_construction_stage_by_id(id)
        #return {'id': id}

    @view_config(route_name='construction_stages_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_stage(self):
        pass
        #id = self.request.matchdict['id']
        ##constructio_stage_schema = ConstructionStageControllerSchema()
        ##try:
        ##    construction_object_deserialized = construction_stage_schema.deserialize(self.request.json_body)
        ##except colander.Invalid as error:
        ##    return Response(status=403, json_body=error.asdict())
        ##except ValueError as date_parse_error:
        ##    return Response(status=403, json_body=date_parse_error.args)
        ##construction_stage_deserialized["id"] = id
        #construction_stage = self.service.get_object(self.request.json_body) #convert_schema_to_object(construction_stage_deserialized)
        #construction_stage = self.service.update_construction_stage(construction_stage)
        #return {'id': construction_stage.construction_stage_id}