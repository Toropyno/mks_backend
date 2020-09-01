import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.services.construction_service import ConstructionService
from mks_backend.serializers.construction_serializer import ConstructionSerializer
from mks_backend.controllers.schemas.construction_schema import ConstructionSchema

from mks_backend.errors.db_basic_error import DBBasicError


class ConstructionController:

    def __init__(self, request):
        self.request = request
        self.service = ConstructionService()
        self.serializer = ConstructionSerializer()
        self.schema = ConstructionSchema()

    @view_config(route_name='constructions', request_method='GET', renderer='json')
    def get_all_constructions(self):
        if self.request.params:
            constructions = self.service.get_all_constructions()  # TODO: refactor when filtration will be good
            # params_schema = ConstructionControllerFilterSchema()
            # try:
            #     params_deserialized = params_schema.deserialize(self.request.GET)
            # except colander.Invalid as error:
            #     return Response(status=403, json_body=error.asdict())
            # except ValueError as date_parse_error:
            #     return Response(status=403, json_body=date_parse_error.args)
            # params = self.service.get_params_from_schema(params_deserialized)
            # constructions = self.service.filter_constructions(params)
        else:
            constructions = self.service.get_all_constructions()

        json = self.serializer.convert_list_to_json(constructions)
        return json

    @view_config(route_name='add_construction', request_method='POST', renderer='json')
    def add_construction(self):
        construction_schema = ConstructionSchema()
        try:
            construction_deserialized = construction_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())

        construction = self.serializer.convert_schema_to_object(construction_deserialized)
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

    @view_config(route_name='construction_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction(self):
        id = self.request.matchdict['id']
        self.service.delete_construction_by_id(id)
        return {'id': id}

    @view_config(route_name='construction_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction(self):
        construction_schema = ConstructionSchema()
        try:
            construction_deserialized = construction_schema.deserialize(self.request.json_body)
            construction_deserialized['id'] = self.request.matchdict['id']
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())

        new_construction = self.serializer.convert_schema_to_object(construction_deserialized)
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

    @view_config(route_name='construction_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction(self):
        id = self.request.matchdict['id']
        construction = self.service.get_construction_by_id(id)
        json = self.serializer.convert_object_to_json(construction)
        return json
