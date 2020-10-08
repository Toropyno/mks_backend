import colander
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from mks_backend.controllers.schemas.construction import ConstructionSchema, ConstructionFilterSchema
from mks_backend.serializers.construction import ConstructionSerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.services.construction import ConstructionService

from mks_backend.errors.colander_error import get_collander_error_dict
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.services.construction_object import ConstructionObjectService


class ConstructionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionService()
        self.serializer = ConstructionSerializer()
        self.schema = ConstructionSchema()
        self.filter_schema = ConstructionFilterSchema()
        self.coordinate_serializer = CoordinateSerializer()
        self.object_service = ConstructionObjectService()

    @view_config(route_name='get_all_constructions', renderer='json')
    def get_all_constructions(self):
        if self.request.params:
            try:
                params_deserialized = self.filter_schema.deserialize(self.request.GET)
            except colander.Invalid as error:
                return Response(status=403, json_body=error.asdict())

            constructions = self.service.filter_constructions(params_deserialized)
        else:
            constructions = self.service.get_all_constructions()

        return self.serializer.convert_list_to_json(constructions)

    @view_config(route_name='add_construction', renderer='json')
    def add_construction(self):
        construction_schema = ConstructionSchema()
        try:
            construction_deserialized = construction_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        coordinate = self.coordinate_serializer.convert_schema_to_object(construction_deserialized)
        construction = self.service.convert_schema_to_object(construction_deserialized)
        construction.coordinate = coordinate
        try:
            self.service.add_construction(construction)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': construction.construction_id}

    @view_config(route_name='delete_construction', renderer='json')
    def delete_construction(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_construction', renderer='json')
    def edit_construction(self):
        construction_schema = ConstructionSchema()
        try:
            construction_deserialized = construction_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        construction_deserialized['id'] = self.request.matchdict['id']

        coordinate = self.coordinate_serializer.convert_schema_to_object(construction_deserialized)
        new_construction = self.service.convert_schema_to_object(construction_deserialized)
        new_construction.coordinate = coordinate
        try:
            self.service.update_construction(new_construction)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': new_construction.construction_id}

    @view_config(route_name='get_construction', renderer='json')
    def get_construction(self):
        id = int(self.request.matchdict['id'])
        construction = self.service.get_construction_by_id(id)

        objects_calculated = self.object_service.get_construction_objects_calculated(id)

        return self.serializer.convert_object_to_json(construction, objects_calculated)
