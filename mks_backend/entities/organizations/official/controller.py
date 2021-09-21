from pyramid.view import view_config, view_defaults
from pyramid.request import Request

from .schema import OfficialSchema, OfficialFilterSchema
from .serializer import OfficialSerializer
from .service import OfficialService


@view_defaults(renderer='json')
class OfficialController:

    def __init__(self, request: Request):
        self.request = request
        self.service = OfficialService()
        self.serializer = OfficialSerializer()

        self.schema = OfficialSchema()
        self.filter_schema = OfficialFilterSchema()

    @view_config(route_name='add_official')
    def add_official(self):
        official_deserialized = self.schema.deserialize(self.request.json_body)
        official = self.serializer.convert_schema_to_object(official_deserialized)

        self.service.add_official(official)
        return {'id': official.officials_id}

    @view_config(route_name='edit_official')
    def edit_official(self):
        id = self.get_id()
        official_deserialized = self.schema.deserialize(self.request.json_body)
        official_deserialized['id'] = id

        official = self.serializer.convert_schema_to_object(official_deserialized)

        self.service.update_official(official)
        return {'id': id}

    @view_config(route_name='delete_official')
    def delete_official(self):
        id = self.get_id()
        self.service.delete_official_by_id(id)
        return {'id': id}

    @view_config(route_name='get_officials_by_organization')
    def get_officials_by_organization(self):
        reflect_vacated_position = self.filter_schema.deserialize(self.request.GET).get('reflectVacatedPosition', True)
        organization_id = self.request.matchdict.get('organization_uuid')

        officials = self.service.get_officials_by_organization(organization_id, reflect_vacated_position)
        return self.serializer.convert_list_to_json(officials)

    @view_config(route_name='get_official_by_id')
    def get_official(self):
        official = self.service.get_official(self.get_id())
        return self.serializer.to_json(official)

    def get_id(self):
        return int(self.request.matchdict.get('id'))
