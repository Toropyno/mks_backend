from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.utils.date_and_time import get_date_iso_string

from .schema import MilitaryUnitExtensionSchema
from .serializer import MilitaryUnitExtensionSerializer
from .service import MilitaryUnitExtensionService


@view_defaults(renderer='json')
class MilitaryUnitExtensionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = MilitaryUnitExtensionService()
        self.serializer = MilitaryUnitExtensionSerializer()
        self.schema = MilitaryUnitExtensionSchema()

    @view_config(route_name='add_military_unit_extension')
    def add_military_unit_extension(self):
        military_unit_extension_deserialized = self.schema.deserialize(self.request.json_body)

        military_unit_extension = self.serializer.to_mapped_object(military_unit_extension_deserialized)
        self.service.add_military_unit_extension(military_unit_extension)
        return HTTPCreated(json_body={'id': military_unit_extension.idMU})

    @view_config(route_name='delete_military_unit_extension')
    def delete_military_unit_extension(self):
        id_ = self.get_id()
        date = get_date_iso_string(self.request.matchdict.get('date'))
        self.service.delete_military_unit_extension_by_id(id_, date)
        return HTTPNoContent()

    @view_config(route_name='edit_military_unit_extension')
    def edit_military_unit_extension(self):
        military_unit_extension_deserialized = self.schema.deserialize(self.request.json_body)
        military_unit_extension_deserialized['idMU'] = self.get_id()
        military_unit_extension_deserialized['date'] = get_date_iso_string(self.request.matchdict.get('date'))

        new_military_unit_extension = self.serializer.to_mapped_object(military_unit_extension_deserialized)
        self.service.update_military_unit_extension(new_military_unit_extension)
        return {'id': new_military_unit_extension.idMU}

    @view_config(route_name='get_military_unit_extension')
    def get_military_unit_extension(self):
        id_ = self.get_id()
        military_unit_extension = self.service.get_military_unit_extension_by_id(id_)
        return self.serializer.to_json(military_unit_extension)

    def get_id(self):
        return int(self.request.matchdict['id'])
