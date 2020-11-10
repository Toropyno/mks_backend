from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.controllers.schemas.work_list.measure_unit import MeasureUnitSchema
from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
from mks_backend.serializers.work_list.measure_unit import MeasureUnitSerializer
from mks_backend.services.work_list.measure_unit import MeasureUnitService


class MeasureUnitController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = MeasureUnitSerializer()
        self.service = MeasureUnitService()
        self.schema = MeasureUnitSchema()

    @view_config(route_name='get_all_measure_units', renderer='json')
    def get_all_measure_units(self):
        measure_units = self.service.get_all_measure_units()
        return self.serializer.convert_list_to_json(measure_units)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_measure_unit', renderer='json')
    def add_measure_unit(self):
        measure_unit_deserialized = self.schema.deserialize(self.request.json_body)

        measure_unit = self.serializer.convert_schema_to_object(measure_unit_deserialized)
        self.service.add_measure_unit(measure_unit)
        return {'id': measure_unit.unit_id}

    @view_config(route_name='get_measure_unit', renderer='json')
    def get_measure_unit(self):
        id = int(self.request.matchdict['id'])
        measure_unit = self.service.get_measure_unit_by_id(id)
        return self.serializer.convert_object_to_json(measure_unit)

    @view_config(route_name='delete_measure_unit', renderer='json')
    def delete_measure_unit(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_measure_unit_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_measure_unit', renderer='json')
    def edit_measure_unit(self):
        id = int(self.request.matchdict['id'])
        measure_unit_deserialized = self.schema.deserialize(self.request.json_body)

        measure_unit_deserialized['id'] = id
        measure_unit = self.serializer.convert_schema_to_object(measure_unit_deserialized)

        self.service.update_measure_unit(measure_unit)
        return {'id': id}