from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.inspections.inspected_object import InspectedObjectSchema
from mks_backend.serializers.construction import ConstructionSerializer
from mks_backend.serializers.inspections.inspected_object import InspectedObjectSerializer
from mks_backend.services.inspections.inspected_object import InspectedObjectService

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class InspectedObjectController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = InspectedObjectSchema()
        self.service = InspectedObjectService()
        self.construction_serializer = ConstructionSerializer()
        self.serializer = InspectedObjectSerializer()

    @view_config(route_name='get_inspected_objects_by_inspection')
    def get_inspected_objects_by_inspection(self):
        inspection_id = int(self.request.matchdict.get('inspection_id'))
        inspected_objects = self.service.get_inspected_objects_by_inspection(inspection_id)
        return self.construction_serializer.convert_list_to_json(inspected_objects)

    @view_config(route_name='delete_inspected_object')
    def delete_inspected_object(self):
        inspection_id = int(self.request.matchdict.get('inspection_id'))
        construction_id = int(self.request.matchdict.get('construction_id'))

        self.service.delete_inspected_object(inspection_id, construction_id)
        return {'inspection_id': inspection_id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_inspected_object')
    def add_inspected_object(self):
        inspection_id = int(self.request.matchdict.get('inspection_id'))

        inspected_objects_deserialized = self.schema.deserialize(self.request.json_body)['constructions']
        inspected_objects = self.serializer.convert_list_to_objects(
            inspection_id, inspected_objects_deserialized
        )

        self.service.add_inspected_objects(inspected_objects)
        return {'inspection_id': inspection_id}