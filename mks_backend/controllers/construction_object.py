from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.controllers.schemas.construction_object import ConstructionObjectSchema
from mks_backend.serializers.construction_object import ConstructionObjectSerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.services.construction_object import ConstructionObjectService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error


class ConstructionObjectController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionObjectService()
        self.serializer = ConstructionObjectSerializer()
        self.schema = ConstructionObjectSchema()
        self.coordinate_serializer = CoordinateSerializer()

    @view_config(route_name='get_construction_objects_by_parent', renderer='json')
    def get_all_construction_objects_by_construction_id(self):
        construction_id = self.request.matchdict['construction_id']
        construction_objects = self.service.get_all_construction_objects_by_construction_id(construction_id)
        return self.serializer.convert_list_to_json(construction_objects)

    @view_config(route_name='get_construction_object', renderer='json')
    def get_construction_object_by_id(self):
        id = int(self.request.matchdict['id'])
        construction_object = self.service.get_construction_object_by_id(id)
        return self.serializer.convert_object_to_json(construction_object)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_construction_object', renderer='json')
    def add_construction_object(self):
        construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        construction_object = self.service.convert_schema_to_object(construction_object_deserialized)

        construction_object.coordinate = self.coordinate_serializer.convert_schema_to_object(
            construction_object_deserialized
        )

        self.service.add_construction_object(construction_object)
        return {'id': construction_object.construction_objects_id}

    @view_config(route_name='delete_construction_object', renderer='json')
    def delete_construction_object(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_construction_object_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_construction_object', renderer='json')
    def edit_construction_object(self):
        construction_object_deserialized = self.schema.deserialize(self.request.json_body)
        construction_object_deserialized['id'] = int(self.request.matchdict['id'])

        construction_object = self.service.convert_schema_to_object(construction_object_deserialized)

        construction_object.coordinate = self.coordinate_serializer.convert_schema_to_object(
            construction_object_deserialized
        )

        self.service.update_construction_object(construction_object)
        return {'id': construction_object.construction_objects_id}
