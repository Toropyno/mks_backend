from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.entities.coordinate import CoordinateSerializer

from .schema import ConstructionObjectSchema
from .serializer import ConstructionObjectSerializer
from .service import ConstructionObjectService


@view_defaults(renderer='json')
class ConstructionObjectController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionObjectService()
        self.serializer = ConstructionObjectSerializer()
        self.schema = ConstructionObjectSchema()
        self.coordinate_serializer = CoordinateSerializer()

    @view_config(route_name='get_construction_objects_by_parent')
    def get_all_construction_objects_by_construction_id(self):
        construction_id = self.request.matchdict['construction_id']
        construction_objects = self.service.get_all_construction_objects_by_construction_id(construction_id)
        return self.serializer.convert_list_to_json(construction_objects)

    @view_config(route_name='get_construction_object')
    def get_construction_object_by_id(self):
        id_ = int(self.request.matchdict['id'])
        construction_object = self.service.get_construction_object_by_id(id_)
        return self.serializer.to_json(construction_object)

    @view_config(route_name='add_construction_object')
    def add_construction_object(self):
        construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        construction_object = self.service.to_mapped_object(construction_object_deserialized)

        construction_object.coordinate = self.coordinate_serializer.to_mapped_object(
            construction_object_deserialized
        )

        self.service.add_construction_object(construction_object)
        return HTTPCreated(json_body={'id': construction_object.construction_objects_id})

    @view_config(route_name='delete_construction_object')
    def delete_construction_object(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_object_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_construction_object')
    def edit_construction_object(self):
        construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        construction_object_deserialized['id'] = int(self.request.matchdict['id'])

        construction_object = self.service.to_mapped_object(construction_object_deserialized)

        construction_object.coordinate = self.coordinate_serializer.to_mapped_object(
            construction_object_deserialized
        )

        self.service.update_construction_object(construction_object)
        return {'id': construction_object.construction_objects_id}
