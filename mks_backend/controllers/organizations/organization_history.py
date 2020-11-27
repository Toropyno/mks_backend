from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.services.organizations.organization_history import OrganizationHistoryService
from mks_backend.serializers.organizations.organization_history import OrganizationHistorySerializer
from mks_backend.controllers.schemas.organizations.organization_history import OrganizationHistorySchema

from mks_backend.errors import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class OrganizationController:

    def __init__(self, request: Request):
        self.request = request
        self.service = OrganizationHistoryService()
        self.serializer = OrganizationHistorySerializer()
        self.schema = OrganizationHistorySchema()

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_organization_history')
    def add_organization_history(self):
        organization_history_deserialized = self.schema.deserialize(self.request.json_body)
        organization_history = self.serializer.to_mapped_object(organization_history_deserialized)

        self.service.add_organization_history(organization_history)
        return {'organizationHistoryId': organization_history.organizations_history_id}

    @handle_db_error
    @view_config(route_name='get_organization_history_by_organization')
    def get_organization_history_by_organization(self):
        organization_uuid = self.request.matchdict.get('organization_uuid')
        history = self.service.get_organization_history_by_organization_uuid(organization_uuid)
        return self.serializer.convert_list_to_json(history)

    @handle_db_error
    @view_config(route_name='delete_organization_history')
    def delete_organization_history(self):
        organization_history_id = int(self.request.matchdict.get('history_id'))

        self.service.delete_organization_history(organization_history_id)
        return {'organizationHistoryId': organization_history_id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='update_organization_history')
    def update_organization_history(self):
        organization_history_deserialized = self.schema.deserialize(self.request.json_body)
        organization_history_deserialized['organizationHistoryId'] = int(self.request.matchdict.get('history_id'))

        organization_history = self.serializer.to_mapped_object(organization_history_deserialized)
        self.service.update_organization_history(organization_history)
        return {'organizationHistoryId': organization_history.organizations_history_id}
