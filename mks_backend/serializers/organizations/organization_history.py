from mks_backend.models.organizations.organization_history import OrganizationHistory
from mks_backend.serializers.utils.date_and_time import get_date_string


class OrganizationHistorySerializer:

    def to_json(self, record: OrganizationHistory):
        return {
            'shortname': record.shortname,
            'fullname': record.fullname,
            'addressActual': record.address_actual,
            'addressLegal': record.address_legal,
            'functions': record.functions,

            'isLegal': record.organization.org_sign,
            'inn': record.inn,
            'kpp': record.kpp,
            'ogrn': record.ogrn,

            'parent': record.organization.parent.shortname if record.organization.parent else None,
            'parentNumber': record.organization.par_number,

            'beginDate': get_date_string(record.begin_date),
            'endDate': get_date_string(record.end_date),
        }

    def convert_list_to_json(self, rootes):
        return list(map(self.to_json, rootes))

    def to_mapped_object(self, history_record: dict, organization_uuid: str = None):
        if not history_record.get('organizationId'):
            # case when we create organization for the first time
            history_record['organizationId'] = organization_uuid

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
            organizations_id=history_record.get('organizationId')
        )

        return history_record
