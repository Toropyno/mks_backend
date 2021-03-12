from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.serializers.constructions.construction_dynamic import ConstructionDynamicSerializer
from mks_backend.services.constructions.construction_dynamic import ConstructionDynamicService
from mks_backend.controllers.schemas.constructions.construction_dynamic import ConstructionDynamicSchema


@view_defaults(renderer='json')
class ConstructionDynamicController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionDynamicService()
        self.serializer = ConstructionDynamicSerializer()
        self.schema = ConstructionDynamicSchema()

    @view_config(route_name='get_dynamics_by_construction')
    def get_dynamics_by_construction(self):
        construction_id = self.request.matchdict.get('construction_id')
        dynamics = self.service.get_construction_dynamics_by_construction_id(construction_id)

        return self.serializer.convert_list_to_json(dynamics)

    @view_config(route_name='add_construction_dynamic')
    def add_construction_dynamic_dynamic(self):
        construction_dynamic_deserialized = self.schema.deserialize(self.request.json_body)
        construction_dynamic = self.serializer.to_mapped_object(construction_dynamic_deserialized)

        self.service.add_construction_dynamic(construction_dynamic)
        return {'id': construction_dynamic.construction_dynamics_id}

    @view_config(route_name='delete_construction_dynamic')
    def delete_construction_dynamic(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_dynamic_by_id(id_)
        return {'id': id_}

    @view_config(route_name='edit_construction_dynamic')
    def edit_construction_dynamic(self):
        construction_dynamic_deserialized = self.schema.deserialize(self.request.json_body)
        construction_dynamic_deserialized['id'] = int(self.request.matchdict['id'])

        new_construction_dynamic = self.serializer.to_mapped_object(construction_dynamic_deserialized)

        self.service.update_construction_dynamic(new_construction_dynamic)
        return {'id': new_construction_dynamic.construction_dynamics_id}

    @view_config(route_name='get_construction_dynamic')
    def get_construction_dynamic(self):
        id_ = int(self.request.matchdict['id'])
        construction_dynamic = self.service.get_construction_dynamic_by_id(id_)
        return self.serializer.to_json(construction_dynamic)
