from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .service import OrganizationService
from .serializer import OrganizationSerializer
from .schema import OrganizationSchema, OrganizationFilterSchema


@view_defaults(renderer='json')
class OrganizationController:

    def __init__(self, request: Request):
        self.request = request
        self.service = OrganizationService()
        self.serializer = OrganizationSerializer()

        self.schema = OrganizationSchema()
        self.filter_schema = OrganizationFilterSchema()

    @view_config(route_name='get_organizations_tree', permission='access.mks_crud_organizations')
    def get_organizations_tree(self):
        reflect_disbanded = self.filter_schema.deserialize(self.request.GET).get('reflectDisbanded', True)
        rootes = self.service.get_rootes(reflect_disbanded)
        return self.serializer.to_json_tree(rootes, reflect_disbanded)

    @view_config(route_name='add_organization', permission='access.mks_crud_organizations')
    def add_organization(self):
        organization_deserialized = self.schema.deserialize(self.request.json_body)
        organization = self.serializer.to_mapped_object(organization_deserialized)

        self.service.add_organization(organization)
        return {'organizationId': organization.organizations_id}

    @view_config(route_name='delete_organization', permission='access.mks_crud_organizations')
    def delete_organization(self):
        organization_uuid = self.request.matchdict.get('organization_uuid')
        new_parent_uuid = self.request.params.get('newParent')

        self.service.delete_organization(organization_uuid, new_parent_uuid)
        return {'organizationId': organization_uuid}

    @view_config(route_name='edit_organization', permission='access.mks_crud_organizations')
    def edit_organization(self):
        edit_data = self.request.json_body.copy()
        organization_uuid = self.request.matchdict['organization_uuid']
        edit_data['organizationId'] = organization_uuid

        organization = self.serializer.to_mapped_object(self.schema.deserialize(edit_data))
        self.service.update_organization(organization)
        return {'organizationId': organization_uuid}