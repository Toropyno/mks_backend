from uuid import uuid4

from mks_backend.models.organizations.organization import Organization
from mks_backend.models.organizations.organization_history import OrganizationHistory
from mks_backend.serializers.organizations.organization_history import OrganizationHistorySerializer


class OrganizationSerializer:

    def __init__(self):
        self.history_serializer = OrganizationHistorySerializer()

    def to_json(self, node: Organization):
        return {
            'name': node.actual.shortname,
            'id': node.organizations_id,
            'parentId': node.parent.organizations_id if node.parent else None,
            'isActive': False if node.actual.end_date else True,
            'history': self.history_serializer.convert_list_to_json(node.history),

            # recursive strategy
            'childs': self.to_json_tree(node.childs)
        }

    def to_json_tree(self, rootes):
        return list(map(self.to_json, rootes))

    def to_mapped_object(self, schema: dict) -> Organization:
        organization = Organization(
            organizations_id=str(uuid4()),
            parent_organizations_id=schema.get('parentId'),
            par_number=schema.get('parentNumber'),
            org_sign=schema.get('isLegal', False)
        )

        history_record = schema.pop('history')
        history_record = OrganizationHistory(
            shortname=history_record.get('shortname'),
            fullname=history_record.get('fullname'),
            address_legal=history_record.get('addressLegal'),
            address_actual=history_record.get('addressActual'),
            functions=history_record.get('functions'),
            inn=history_record.get('inn'),
            kpp=history_record.get('kpp'),
            ogrn=history_record.get('ogrn'),
            begin_date=history_record.get('beginDate'),
            end_date=history_record.get('endDate'),
            organizations_id=organization.organizations_id
        )

        organization.history = [history_record]
        return organization
