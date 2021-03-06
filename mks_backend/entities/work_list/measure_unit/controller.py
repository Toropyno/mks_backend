from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import MeasureUnitSchema
from .serializer import MeasureUnitSerializer
from .service import MeasureUnitService


@view_defaults(renderer='json')
class MeasureUnitController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = MeasureUnitSerializer()
        self.service = MeasureUnitService()
        self.schema = MeasureUnitSchema()

    @view_config(route_name='get_all_measure_units')
    def get_all_measure_units(self):
        measure_units = self.service.get_all_measure_units()
        return self.serializer.convert_list_to_json(measure_units)

    @view_config(route_name='add_measure_unit')
    def add_measure_unit(self):
        measure_unit_deserialized = self.schema.deserialize(self.request.json_body)

        measure_unit = self.serializer.to_mapped_object(measure_unit_deserialized)
        self.service.add_measure_unit(measure_unit)
        return HTTPCreated(json_body={'id': measure_unit.unit_id})

    @view_config(route_name='get_measure_unit')
    def get_measure_unit(self):
        id_ = int(self.request.matchdict['id'])
        measure_unit = self.service.get_measure_unit_by_id(id_)
        return self.serializer.to_json(measure_unit)

    @view_config(route_name='delete_measure_unit')
    def delete_measure_unit(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_measure_unit_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_measure_unit')
    def edit_measure_unit(self):
        id_ = int(self.request.matchdict['id'])
        measure_unit_deserialized = self.schema.deserialize(self.request.json_body)

        measure_unit_deserialized['id'] = id_
        measure_unit = self.serializer.to_mapped_object(measure_unit_deserialized)

        self.service.update_measure_unit(measure_unit)
        return {'id': id_}
