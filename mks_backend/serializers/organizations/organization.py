from mks_backend.models.organizations.organization import Organization
from mks_backend.serializers.organizations.organization_history import OrganizationHistorySerializer


class OrganizationSerializer:

    def __init__(self):
        self.history_serializer = OrganizationHistorySerializer()

    def to_json(self, node: Organization):
        return {
            'name': node.actual.shortname,
            'id': str(node.organizations_id),
            'parentId': str(node.parent.organizations_id) if node.parent else None,
            'isActive': False if node.actual.end_date else True,
            'history': self.history_serializer.convert_list_to_json(node.history),

            # recursive strategy
            'childs': self.to_json_tree(node.childs)
        }

    def to_json_tree(self, rootes):
        return list(map(self.to_json, rootes))
