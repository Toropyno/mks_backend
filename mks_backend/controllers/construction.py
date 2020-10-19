from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.controllers.schemas.construction import ConstructionSchema, ConstructionFilterSchema
from mks_backend.serializers.construction import ConstructionSerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.services.construction import ConstructionService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error


class ConstructionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionService()
        self.serializer = ConstructionSerializer()
        self.schema = ConstructionSchema()
        self.filter_schema = ConstructionFilterSchema()
        self.coordinate_serializer = CoordinateSerializer()

    @handle_colander_error
    @view_config(route_name='get_all_constructions', renderer='json')
    def get_all_constructions(self):
        if self.request.params:
            params_deserialized = self.filter_schema.deserialize(self.request.GET)
            constructions = self.service.filter_constructions(params_deserialized)
        else:
            constructions = self.service.get_all_constructions()

        return self.serializer.convert_list_to_json(constructions)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_construction', renderer='json')
    def add_construction(self):
        construction_deserialized = self.schema.deserialize(self.request.json_body)

        coordinate = self.coordinate_serializer.convert_schema_to_object(construction_deserialized)
        construction = self.service.convert_schema_to_object(construction_deserialized)
        construction.coordinate = coordinate

        self.service.add_construction(construction)
        return {'id': construction.construction_id}

    @view_config(route_name='delete_construction', renderer='json')
    def delete_construction(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_construction', renderer='json')
    def edit_construction(self):
        construction_deserialized = self.schema.deserialize(self.request.json_body)
        construction_deserialized['id'] = int(self.request.matchdict['id'])

        coordinate = self.coordinate_serializer.convert_schema_to_object(construction_deserialized)
        new_construction = self.service.convert_schema_to_object(construction_deserialized)
        new_construction.coordinate = coordinate

        self.service.update_construction(new_construction)
        return {'id': new_construction.construction_id}

    @view_config(route_name='get_construction', renderer='json')
    def get_construction(self):
        id = int(self.request.matchdict['id'])
        construction = self.service.get_construction_by_id(id)
        return self.serializer.convert_object_to_json(construction)
