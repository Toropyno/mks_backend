from uuid import uuid4

from mks_backend.models.organizations.organization import Organization
from mks_backend.serializers.organizations.official import OfficialSerializer
from mks_backend.serializers.organizations.organization_document import OrganizationDocumentSerializer
from mks_backend.serializers.organizations.organization_history import OrganizationHistorySerializer


class OrganizationSerializer:

    def __init__(self):
        self.history_serializer = OrganizationHistorySerializer()
        self.oficial_serializer = OfficialSerializer()
        self.document = OrganizationDocumentSerializer()


    def to_json(self, node: Organization) -> dict:
        return {
            'organizationId': node.organizations_id,
            'parentId': node.parent.organizations_id if node.parent else None,
            'shortname': node.actual.shortname,
            'fullname': node.actual.fullname,
            'isActive': False if node.actual.end_date else True,
            'history': self.history_serializer.convert_list_to_json(node.history),
            'oficials': self.oficial_serializer.convert_list_to_json(node.officials) if node.officials else [],
            'organizationDocuments': self.document.convert_list_to_json(node.organization_documents),

            # recursive strategy
            'children': self.to_json_tree(node.children),
        }

    def to_json_tree(self, rootes: list) -> list:
        return list(map(self.to_json, rootes))

    def to_mapped_object(self, schema: dict) -> Organization:
        organization = Organization(
            organizations_id=str(uuid4()),
            parent_organizations_id=schema.get('parentId'),
            par_number=schema.get('parentNumber'),
            org_sign=schema.get('isLegal')
        )

        history_record = self.history_serializer.to_mapped_object(
            schema.pop('history'), organization.organizations_id
        )

        organization.history = [history_record]
        return organization
