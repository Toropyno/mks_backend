from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.constructions import ConstructionSchema, ConstructionFilterSchema
from mks_backend.serializers.constructions import ConstructionSerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.services.constructions import ConstructionService
from mks_backend.services.geoobject.geo_object import GeoObjectService
from mks_backend.services.geoobject.geo_object__cross__user import GeoObjectCrossUserService


@view_defaults(renderer='json')
class ConstructionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionService()
        self.geo_object_service = GeoObjectCrossUserService()
        self.serializer = ConstructionSerializer()
        self.schema = ConstructionSchema()
        self.filter_schema = ConstructionFilterSchema()
        self.coordinate_serializer = CoordinateSerializer()

    @view_config(route_name='get_all_constructions', permission='access.mks_crud_isp')
    def get_all_constructions(self):
        if self.request.params:
            params_deserialized = self.filter_schema.deserialize(self.request.GET)
            constructions = self.service.filter_constructions(params_deserialized)
        else:
            constructions = self.service.get_all_constructions()

        return self.serializer.convert_list_to_json(constructions)

    @view_config(route_name='add_construction', permission='access.mks_crud_isp')
    def add_construction(self):
        construction_deserialized = self.schema.deserialize(self.request.json_body)

        coordinate = self.coordinate_serializer.convert_schema_to_object(construction_deserialized)
        construction = self.service.convert_schema_to_object(construction_deserialized)
        if (construction.geo_object):
            construction.geo_object.coordinate = coordinate

        self.service.add_construction(construction)
        return {'id': construction.construction_id}

    @view_config(route_name='delete_construction', permission='access.mks_crud_isp')
    def delete_construction(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_construction', permission='access.mks_crud_isp')
    def edit_construction(self):
        construction_deserialized = self.schema.deserialize(self.request.json_body)
        construction_deserialized['id'] = int(self.request.matchdict['id'])

        coordinate = self.coordinate_serializer.convert_schema_to_object(construction_deserialized)
        new_construction = self.service.convert_schema_to_object(construction_deserialized)
        if (new_construction.geo_object):
            new_construction.geo_object.coordinate = coordinate
       # new_construction.coordinate = coordinate

        self.service.update_construction(new_construction)
        return {'id': new_construction.construction_id}

    @view_config(route_name='get_construction', permission='access.mks_crud_isp')
    def get_construction(self):
        id = int(self.request.matchdict['id'])
        construction = self.service.get_construction_by_id(id)
        return self.serializer.to_json(construction)
