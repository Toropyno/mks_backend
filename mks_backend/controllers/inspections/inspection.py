from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.inspections.inspection import InspectionSchema
from mks_backend.serializers.inspections.inspection import InspectionSerializer
from mks_backend.services.inspections.inspection import InspectionService

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class InspectionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = InspectionService()
        self.serializer = InspectionSerializer()
        self.schema = InspectionSchema()

    @handle_colander_error
    @view_config(route_name='get_all_inspections')
    def get_all_inspections(self):
        inspections = self.service.get_inspections()
        return self.serializer.convert_list_to_json(inspections)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_inspection')
    def add_inspection(self):
        inspection_deserialized = self.schema.deserialize(self.request.json_body)

        inspection = self.serializer.convert_schema_to_object(inspection_deserialized)
        self.service.add_inspection(inspection)
        return {'id': inspection.inspections_id}

    @view_config(route_name='delete_inspection')
    def delete_inspection(self):
        id = self.get_id()
        self.service.delete_inspection_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_inspection')
    def edit_inspection(self):
        inspection_deserialized = self.schema.deserialize(self.request.json_body)
        inspection_deserialized['id'] = self.get_id()

        new_inspection = self.serializer.convert_schema_to_object(inspection_deserialized)
        self.service.update_inspection(new_inspection)
        return {'id': new_inspection.inspections_id}

    @view_config(route_name='get_inspection')
    def get_inspection(self):
        id = self.get_id()
        inspection = self.service.get_inspection_by_id(id)
        return self.serializer.to_json(inspection)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
