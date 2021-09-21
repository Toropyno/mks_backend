from .model import OrganizationHistory
from mks_backend.utils.date_and_time import get_date_string


class OrganizationHistorySerializer:

    def to_json(self, record: OrganizationHistory) -> dict:
        return {
            'organizationHistoryId': record.organizations_history_id,
            'shortname': record.shortname,
            'fullname': record.fullname,
            'addressActual': record.address_actual,
            'addressLegal': record.address_legal,
            'functions': record.functions,

            'inn': record.inn,
            'kpp': record.kpp,
            'ogrn': record.ogrn,

            'beginDate': get_date_string(record.begin_date),
            'endDate': get_date_string(record.end_date),
        }

    def convert_list_to_json(self, history_records: list) -> list:
        return list(map(self.to_json, history_records))

    def to_mapped_object(self, history_record: dict, organization_uuid: str = None) -> OrganizationHistory:
        if not history_record.get('organizationId'):
            # case when we create organization for the first time
            history_record['organizationId'] = organization_uuid

        history_record = OrganizationHistory(
            organizations_history_id=history_record.get('organizationHistoryId'),
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
