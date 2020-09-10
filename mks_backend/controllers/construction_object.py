import colander
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request

from mks_backend.services.construction_object import ConstructionObjectService
from mks_backend.serializers.construction_object import ConstructionObjectSerializer
from mks_backend.controllers.schemas.construction_object import ConstructionObjectSchema
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.location import LocationSerializer


class ConstructionObjectController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionObjectService()
        self.serializer = ConstructionObjectSerializer()
        self.schema = ConstructionObjectSchema()


    @view_config(route_name='construction_objects', request_method='GET', renderer='json')
    def get_all_construction_objects_by_construction_id(self):
        construction_id = self.request.matchdict['construction_id']
        construction_objects = self.service.get_all_construction_objects_by_construction_id(construction_id)
        return self.serializer.convert_list_to_json(construction_objects)

    @view_config(route_name='add_construction_object', request_method='POST', renderer='json')
    def add_construction_object(self):
        try:
            construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)

        location = LocationSerializer.convert_schema_to_object(construction_object_deserialized)
        construction_object = self.serializer.convert_schema_to_object(construction_object_deserialized)
        construction_object.location = location

        try:
            self.service.add_construction_object(construction_object)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': construction_object.construction_objects_id}

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction_object(self):
        id = int(self.request.matchdict['id'])
        construction_object = self.service.get_construction_object_by_id(id)
        return self.serializer.convert_object_to_json(construction_object)

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction_object(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_object_by_id(id)
        return {'id': id}

    @view_config(route_name='construction_objects_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction_object(self):
        id = int(self.request.matchdict['id'])
        try:
            construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)

        construction_object_deserialized['id'] = id

        location = LocationSerializer.convert_schema_to_object(construction_object_deserialized)
        construction_object = self.serializer.convert_schema_to_object(construction_object_deserialized)
        construction_object.location = location

        try:
            self.service.update_construction_object(construction_object)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': id}
