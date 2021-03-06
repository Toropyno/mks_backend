from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.entities.constructions.construction import ConstructionSerializer
from mks_backend.entities.coordinate import CoordinateSerializer

from .schema import ConstructionFilterSchema, ConstructionSchema
from .service import ConstructionService


@view_defaults(renderer='json')
class ConstructionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionService()
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

        coordinate = self.coordinate_serializer.to_mapped_object(construction_deserialized)
        construction = self.service.to_mapped_object(construction_deserialized)
        construction.coordinate = coordinate

        self.service.add_construction(construction)
        return HTTPCreated(json_body={'id': construction.construction_id})

    @view_config(route_name='delete_construction', permission='access.mks_crud_isp')
    def delete_construction(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_construction', permission='access.mks_crud_isp')
    def edit_construction(self):
        construction_deserialized = self.schema.deserialize(self.request.json_body)
        construction_deserialized['id'] = int(self.request.matchdict['id'])

        new_construction = self.service.to_mapped_object(construction_deserialized)
        new_construction.coordinate = self.coordinate_serializer.to_mapped_object(construction_deserialized)

        self.service.update_construction(new_construction)
        return {'id': new_construction.construction_id}

    @view_config(route_name='get_construction', permission='access.mks_crud_isp')
    def get_construction(self):
        id_ = int(self.request.matchdict['id'])
        construction = self.service.get_construction_by_id(id_)
        return self.serializer.to_json(construction)
