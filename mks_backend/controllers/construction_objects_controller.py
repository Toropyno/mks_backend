import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.services.construction_objects_service import ConstructionObjectService
# from mks_backend.serializers.construction_objects_serializer import ConstructionObjectsSerializer


class ConstructionObjectsController(object):

    def __init__(self, request):
        self.request = request
        self.service = ConstructionObjectService()
        # self.serializer = ConstructionObjectsSerializer()

    @view_config(route_name='add_construction_object', request_method='POST', renderer='json')
    def add_construction_object(self):
        pass
        # # construction_object_schema = ConstructionOjectControllerSchema()
        # # try:
        # #    construction_object_deserialized = construction_object_schema.deserialize(self.request.json_body)
        # # except colander.Invalid as error:
        # #    return Response(status=403, json_body=error.asdict())
        # # except ValueError as date_parse_error:
        # #    return Response(status=403, json_body=date_parse_error.args)
        # construction_object = self.service.get_object(
        #     self.request.json_body)  # convert_schema_to_object(construction_object_deserialized)
        # self.service.add_construction_object(construction_object)
        # return {'id': construction_object.construction_object_id}

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_object(self):
        pass
        # id = self.request.matchdict['id']
        # construction_object = self.service.get_construction_object_by_id(id)
        # json = self.serializer.convert_object_to_json(construction_object)
        # return json

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        pass
        # id = self.request.matchdict['id']
        # self.service.delete_construction_object_by_id(id)
        # return {'id': id}

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_object(self):
        pass
        # id = self.request.matchdict['id']
        ##construction_object__schema = ConstructionObjectControllerSchema()
        ##try:
        ##    construction_object_deserialized = construction_object_schema.deserialize(self.request.json_body)
        ##except colander.Invalid as error:
        ##    return Response(status=403, json_body=error.asdict())
        ##except ValueError as date_parse_error:
        ##    return Response(status=403, json_body=date_parse_error.args)
        ##construction_object_deserialized["id"] = id
        # construction_object = self.service.get_object(self.request.json_body) #convert_schema_to_object(construction_object_deserialized)
        # construction_object = self.service.update_construction_object(construction_object)
        # return {'id': construction_object.construction_object_id}
