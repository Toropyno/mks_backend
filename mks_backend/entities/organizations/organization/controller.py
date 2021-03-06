from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import OrganizationFilterSchema, OrganizationSchema
from .serializer import OrganizationSerializer
from .service import OrganizationService


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
        roots = self.service.get_roots()
        return self.serializer.to_json_tree(roots)

    @view_config(route_name='get_organizations_filter')
    def get_organizations_filter(self):
        filter_fields = self.filter_schema.deserialize(self.request.params)
        return self.service.get_all_organizations(filter_fields)

    @view_config(route_name='add_organization', permission='access.mks_crud_organizations')
    def add_organization(self):
        organization_deserialized = self.schema.deserialize(self.request.json_body)
        organization = self.serializer.to_mapped_object(organization_deserialized)
        self.service.add_organization(organization)
        return HTTPCreated(json_body={'organizationId': organization.organizations_id})

    @view_config(route_name='delete_organization', permission='access.mks_crud_organizations')
    def delete_organization(self):
        organization_uuid = self.request.matchdict.get('organization_uuid')
        new_parent_uuid = self.request.params.get('newParent')

        self.service.delete_organization(organization_uuid, new_parent_uuid)
        return HTTPNoContent()

    @view_config(route_name='edit_organization', permission='access.mks_crud_organizations')
    def edit_organization(self):
        edit_data = self.request.json_body.copy()
        organization_uuid = self.request.matchdict['organization_uuid']
        edit_data['organizationId'] = organization_uuid

        organization = self.serializer.to_mapped_object(self.schema.deserialize(edit_data))
        self.service.update_organization(organization)
        return {'organizationId': organization_uuid}
