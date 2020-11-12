from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.organizations.official import Official
from mks_backend.serializers.utils.date_and_time import get_date_string


class OfficialSerializer:

    @classmethod
    @serialize_error_handler
    def to_json(self, oficial: Official) -> dict:
        return {
            'id': oficial.officials_id,
            'positionName': oficial.position_name,
            'organizationId': oficial.organizations_id,

            'militaryRankId': oficial.military_ranks_id,
            # 'militaryRank': MilitaryRank.to_json(oficial.military_ranks_id),

            'surname': oficial.surname,
            'firstName': oficial.firstname,
            'middleName': oficial.middlename,
            'beginDate': get_date_string(oficial.begin_date),
            'endDate': get_date_string(oficial.end_date),
            'phone': oficial.phone,
            'secureСhannel': oficial.secure_channel,
            'email': oficial.email,
            'note': oficial.note,
        }

    def convert_list_to_json(self, oficials: list) -> list:
        return list(map(self.to_json, oficials))

    def convert_schema_to_object(self, schema_dict: dict) -> Official:
        official = Official()

        official.officials_id = schema_dict.get('id')
        official.position_name = schema_dict.get('positionName')

        official.organizations_id = schema_dict.get('organizationId')
        official.military_ranks_id = schema_dict.get('militaryRankId')

        official.surname = schema_dict.get('surname')
        official.firstname = schema_dict.get('firstName')
        official.middlename = schema_dict.get('middleName')

        official.begin_date = schema_dict.get('beginDate')
        official.end_date = schema_dict.get('endDate')

        official.phone = schema_dict.get('phone')
        official.email = schema_dict.get('email')

        official.secure_channel = schema_dict.get('secureСhannel')
        official.note = schema_dict.get('note')

        return official
