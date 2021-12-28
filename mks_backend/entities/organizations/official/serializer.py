from .model import Official
from mks_backend.entities.organizations.military_rank import MilitaryRankSerializer
from mks_backend.entities.organizations.class_rank import ClassRankSerializer
from mks_backend.utils.date_and_time import get_date_string
from mks_backend.entities.filestorage import FileStorageSerializer

from mks_backend.errors import serialize_error_handler


class OfficialSerializer:

    @classmethod
    @serialize_error_handler
    def to_json(cls, official: Official) -> dict:
        return {
            'id': official.officials_id,
            'positionName': official.position_name,
            'organizationId': official.organizations_id,
            'militaryRank': MilitaryRankSerializer.to_json(official.military_rank),
            'surname': official.surname,
            'firstName': official.firstname,
            'middleName': official.middlename,
            'beginDate': get_date_string(official.begin_date),
            'endDate': get_date_string(official.end_date),
            'phone': official.phone,
            'secureChannel': official.secure_channel,
            'email': official.email,
            'note': official.note,
            'classRank': ClassRankSerializer.to_json(official.class_rank),
            'filestorage': FileStorageSerializer.to_json(official.filestorage)
        }

    def convert_list_to_json(self, oficials: list) -> list:
        return list(map(self.to_json, oficials))

    def convert_schema_to_object(self, schema_dict: dict) -> Official:
        official = Official()

        official.officials_id = schema_dict.get('id')
        official.position_name = schema_dict.get('positionName')

        official.organizations_id = schema_dict.get('organizationId')
        official.military_ranks_id = schema_dict.get('militaryRank')

        official.surname = schema_dict.get('surname')
        official.firstname = schema_dict.get('firstName')
        official.middlename = schema_dict.get('middleName')

        official.begin_date = schema_dict.get('beginDate')
        official.end_date = schema_dict.get('endDate')

        official.phone = schema_dict.get('phone')
        official.email = schema_dict.get('email')

        official.secure_channel = schema_dict.get('secureChannel')
        official.note = schema_dict.get('note')

        official.class_ranks_id = schema_dict.get('classRank'),
        official.idfilestorage = schema_dict.get('filestorage')

        return official
