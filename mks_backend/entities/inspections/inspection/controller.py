from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import InspectionFilterSchema, InspectionSchema
from .serializer import InspectionSerializer
from .service import InspectionService


@view_defaults(renderer='json')
class InspectionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = InspectionService()
        self.serializer = InspectionSerializer()
        self.schema = InspectionSchema()
        self.filter_schema = InspectionFilterSchema()

    @view_config(route_name='get_all_inspections', permission='access.mks_crud_inspections')
    def get_all_inspections(self):
        filter_params = self.filter_schema.deserialize(self.request.GET)
        inspections = self.service.get_inspections(filter_params)
        return self.serializer.convert_list_to_json(inspections)

    @view_config(route_name='add_inspection', permission='access.mks_crud_inspections')
    def add_inspection(self):
        inspection_deserialized = self.schema.deserialize(self.request.json_body)

        inspection = self.serializer.to_mapped_object(inspection_deserialized)
        self.service.add_inspection(inspection)
        return HTTPCreated(json_body={'id': inspection.inspections_id})

    @view_config(route_name='delete_inspection', permission='access.mks_crud_inspections')
    def delete_inspection(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_inspection_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_inspection', permission='access.mks_crud_inspections')
    def edit_inspection(self):
        inspection_deserialized = self.schema.deserialize(self.request.json_body)
        inspection_deserialized['id'] = int(self.request.matchdict['id'])

        new_inspection = self.serializer.to_mapped_object(inspection_deserialized)
        self.service.update_inspection(new_inspection)
        return {'id': new_inspection.inspections_id}

    @view_config(route_name='get_inspection', permission='access.mks_crud_inspections')
    def get_inspection(self):
        id_ = int(self.request.matchdict['id'])
        inspection = self.service.get_inspection_by_id(id_)
        return self.serializer.to_json(inspection)
