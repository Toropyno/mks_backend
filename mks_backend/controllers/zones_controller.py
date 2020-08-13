import colander
from pyramid.view import view_config
from pyramid.response import Response

#from mks_backend.services.zones_service import ZonesServic
#from mks_backend.serializers.zones_serializer import ZonesSerializer


class ConstructionStagesController(object):

    def __init__(self, request):
        self.request = request
        self.service = None #ZonesService()
        self.serializer = None #ZonesSerializer()

    @view_config(route_name='zones', request_method='GET', renderer='json')
    def get_all_zones(self):
        pass
        #zones_array = self.service.get_all_zones()
        #json = self.serializer.convert_list_to_json(zones_array)
        #return json

    @view_config(route_name='add_zone', request_method='POST', renderer='json')
    def add_zone(self):
        pass
        ##zone_schema = ConstructionStagetControllerSchema()
        ##try:
        ##    zone_deserialized = zone_schema.deserialize(self.request.json_body)
        ##except colander.Invalid as error:
        ##    return Response(status=403, json_body=error.asdict())
        ##except ValueError as date_parse_error:
        ##    return Response(status=403, json_body=date_parse_error.args)
        #zone = self.service.get_object(self.request.json_body)#convert_schema_to_object(zone_deserialized)
        #self.service.add_zone(zone)
        #return {'id': zone.zone_id}

    @view_config(route_name='zones_delete_change_and_view', request_method='GET', renderer='json')
    def get_zone(self):
        pass
        #id = self.request.matchdict['id']
        #zone = self.service.get_zone_by_id(id)
        #json = self.serializer.convert_object_to_json(zone)
        #return json

    @view_config(route_name='zones_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        pass
        #id = self.request.matchdict['id']
        #self.service.delete_zone_by_id(id)
        #return {'id': id}

    @view_config(route_name='zones_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_zone(self):
        pass
        #id = self.request.matchdict['id']
        ##constructio_stage_schema = ConstructionStageControllerSchema()
        ##try:
        ##    construction_object_deserialized = zone_schema.deserialize(self.request.json_body)
        ##except colander.Invalid as error:
        ##    return Response(status=403, json_body=error.asdict())
        ##except ValueError as date_parse_error:
        ##    return Response(status=403, json_body=date_parse_error.args)
        ##zone_deserialized["id"] = id
        #zone = self.service.get_object(self.request.json_body) #convert_schema_to_object(zone_deserialized)
        #zone = self.service.update_zone(zone)
        #return {'id': zone.zone_id}