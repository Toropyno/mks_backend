from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.services.organizations.organization import OrganisationService
from mks_backend.serializers.organizations.organization import OrganizationSerializer


@view_defaults(renderer='json')
class OrganizationController:

    def __init__(self, request: Request):
        self.request = request
        self.service = OrganisationService()
        self.serializer = OrganizationSerializer()

    @view_config(route_name='get_organizations_tree')
    def get_organizations_tree(self):
        rootes = self.service.get_rootes()
        return self.serializer.to_json_tree(rootes)

    @view_config(route_name='delete_organization')
    def delete_organization(self):
        organization_uuid = self.request.matchdict.get('organization_uuid')
        new_parent_uuid = self.request.params.get('newParent')

        self.service.delete_organization(organization_uuid, new_parent_uuid)
        return {'organizationId': organization_uuid}
