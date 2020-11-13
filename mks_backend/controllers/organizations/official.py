from pyramid.view import view_config, view_defaults
from pyramid.request import Request

from mks_backend.controllers.schemas.organizations.official import OfficialSchema
from mks_backend.serializers.organizations.official import OfficialSerializer
from mks_backend.services.organizations.official import OfficialService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error


@view_defaults(renderer='json')
class OfficialController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = OfficialSchema()
        self.service = OfficialService()
        self.serializer = OfficialSerializer()

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_official')
    def add_official(self):
        official_deserialized = self.schema.deserialize(self.request.json_body)
        official = self.serializer.convert_schema_to_object(official_deserialized)

        self.service.add_official(official)
        return {'id': official.officials_id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_official')
    def edit_official(self):
        id = int(self.request.matchdict['id'])
        official_deserialized = self.schema.deserialize(self.request.json_body)
        official_deserialized['id'] = id

        official = self.serializer.convert_schema_to_object(official_deserialized)

        self.service.update_official(official)
        return {'id': id}

    @view_config(route_name='delete_official')
    def delete_official(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_official_by_id(id)
        return {'id': id}

    @handle_db_error
    @view_config(route_name='get_officials_by_organization')
    def get_officials_by_organization(self):
        organization_id = self.request.matchdict['organization_uuid']
        officials = self.service.get_officials_by_organization(organization_id)
        return self.serializer.convert_list_to_json(officials)
