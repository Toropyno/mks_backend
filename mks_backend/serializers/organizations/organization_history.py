from mks_backend.models.organizations.organizations_history import OrganizationHistory
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
