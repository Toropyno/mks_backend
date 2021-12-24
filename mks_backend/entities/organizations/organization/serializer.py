from typing import List
from uuid import uuid4

from .model import Organization
from mks_backend.entities.organizations.organization_history import OrganizationHistorySerializer

from mks_backend.errors import serialize_error_handler


class OrganizationSerializer:

    def __init__(self):
        self.history_serializer = OrganizationHistorySerializer()

    def to_json(self, node: Organization) -> dict:
        return {
            'organizationId': node.organizations_id,
            'parentId': node.parent.organizations_id if node.parent else None,
            'parentName': node.parent.shortname if node.parent else None,
            'parentNumber': node.par_number,
            'label': node.actual.shortname,
            'isActive': node.is_active,
            'isLegal': node.org_sign,
            'children': self.to_json_tree(node.children),
        }

    def to_json_tree(self, roots: List[Organization]) -> List[dict]:
        return [self.to_json(root) for root in roots]

    def to_mapped_object(self, schema: dict) -> Organization:
        organization = Organization(
            organizations_id=schema.get('organizationId', str(uuid4())),
            parent_organizations_id=schema.get('parentId'),
            par_number=schema.get('parentNumber'),
            org_sign=schema.get('isLegal')
        )

        if schema.get('history'):
            # case when we create organization for the first time
            history_record = self.history_serializer.to_mapped_object(
                schema.pop('history'), organization.organizations_id
            )
            organization.history = [history_record]

        return organization

    @classmethod
    @serialize_error_handler
    def to_simple_json(cls, organization: Organization):
        return {
            'organizationId': organization.organizations_id,
            'label': organization.actual.shortname
        }
