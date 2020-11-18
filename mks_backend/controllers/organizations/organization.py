from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.services.organizations.organization import OrganisationService
from mks_backend.serializers.organizations.organization import OrganizationSerializer
from mks_backend.controllers.schemas.organizations.organization import (
    OrganizationSchema,
    OrganizationPatchSchema,
    OrganizationFilterSchema,
)

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class OrganizationController:

    def __init__(self, request: Request):
        self.request = request
        self.service = OrganisationService()
        self.serializer = OrganizationSerializer()

        self.schema = OrganizationSchema()
        self.patch_schema = OrganizationPatchSchema()
        self.filter_schema = OrganizationFilterSchema()

    @view_config(route_name='get_organizations_tree')
    def get_organizations_tree(self):
        reflect_disbanded = self.filter_schema.deserialize(self.request.GET).get('reflectDisbanded', True)
        rootes = self.service.get_processed_rootes(reflect_disbanded)
        return self.serializer.to_json_tree(rootes, reflect_disbanded)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_organization')
    def add_organization(self):
        organization_deserialized = self.schema.deserialize(self.request.json_body)
        organization = self.serializer.to_mapped_object(organization_deserialized)

        self.service.add_organization(organization)
        return {'organizationId': organization.organizations_id}

    @handle_db_error
    @view_config(route_name='delete_organization')
    def delete_organization(self):
        organization_uuid = self.request.matchdict.get('organization_uuid')
        new_parent_uuid = self.request.params.get('newParent')

        self.service.delete_organization(organization_uuid, new_parent_uuid)
        return {'organizationId': organization_uuid}

    @handle_db_error
    @view_config(route_name='move_organization')
    def move_organization(self):
        move_params = self.patch_schema.deserialize(self.request.json_body)

        self.service.set_node_new_parent(move_params['organizationId'], move_params['parentId'])
        return move_params
