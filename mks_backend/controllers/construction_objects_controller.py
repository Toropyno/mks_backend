from pyramid.view import view_config
from pyramid.response import Response
import colander

from mks_backend.services.construction_object_service import ConstructionObjectService
from mks_backend.serializers.construction_object_serializer import ConstructionObjectSerializer
from mks_backend.controllers.schemas.construction_objects_schema import ConstructionObjectsSchema


class ConstructionObjectsController(object):

    def __init__(self, request):
        self.request = request
        self.service = ConstructionObjectService()
        self.serializer = ConstructionObjectSerializer()
        self.schema = ConstructionObjectsSchema()

    @view_config(route_name='construction_objects', request_method='GET', renderer='json')
    def get_all_construction_objects_by_construction_id(self):
        construction_id = self.request.matchdict['construction_id']
        construction_objects = self.service.get_all_construction_objects_by_construction_id(construction_id)
        json = self.serializer.convert_list_to_json(construction_objects)
        return json

    @view_config(route_name='add_construction_object', request_method='POST', renderer='json')
    def add_construction_object(self):
        try:
            construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        construction_object = self.serializer.convert_schema_to_object(construction_object_deserialized)
        try:
            self.service.add_construction_object(construction_object)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})
        return {'id': construction_object.construction_objects_id}

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_object(self):
        id = self.request.matchdict['id']
        construction_object = self.service.get_construction_object_by_id(id)
        json = self.serializer.convert_object_to_json(construction_object)
        return json

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        id = self.request.matchdict['id']
        self.service.delete_construction_object_by_id(id)
        return {'id': id}

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_object(self):
        id = self.request.matchdict['id']
        try:
            construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        construction_object_deserialized['id'] = id
        construction_object = self.serializer.convert_schema_to_object(construction_object_deserialized)
        try:
            self.service.update_construction_object(construction_object)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})
        return {'id': id}
