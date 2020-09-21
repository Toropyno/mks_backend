import colander
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from mks_backend.controllers.schemas.construction_object import ConstructionObjectSchema
from mks_backend.errors.colander_error import get_collander_error_dict
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.construction_object import ConstructionObjectSerializer
from mks_backend.serializers.location import LocationSerializer
from mks_backend.services.construction_object import ConstructionObjectService


class ConstructionObjectController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionObjectService()
        self.serializer = ConstructionObjectSerializer()
        self.schema = ConstructionObjectSchema()
        self.coordinate_serializer = LocationSerializer()

    @view_config(route_name='get_construction_objects_by_parent', renderer='json')
    def get_all_construction_objects_by_construction_id(self):
        construction_id = self.request.matchdict['construction_id']
        construction_objects = self.service.get_all_construction_objects_by_construction_id(construction_id)
        return self.serializer.convert_list_to_json(construction_objects)

    @view_config(route_name='add_construction_object', renderer='json')
    def add_construction_object(self):
        try:
            construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)

        construction_object = self.service.convert_schema_to_object(construction_object_deserialized)

        construction_object.coordinate = self.coordinate_serializer.convert_schema_to_object(
            construction_object_deserialized
        )

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

    @view_config(route_name='get_construction_object', renderer='json')
    def get_construction_object(self):
        id = int(self.request.matchdict['id'])
        construction_object = self.service.get_construction_object_by_id(id)
        return self.serializer.convert_object_to_json(construction_object)

    @view_config(route_name='delete_construction_object', renderer='json')
    def delete_construction_object(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_object_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_construction_object', renderer='json')
    def edit_construction_object(self):
        id = int(self.request.matchdict['id'])
        try:
            construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)

        construction_object_deserialized['id'] = id

        construction_object = self.service.convert_schema_to_object(construction_object_deserialized)

        construction_object.coordinate = self.coordinate_serializer.convert_schema_to_object(
            construction_object_deserialized
        )

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
