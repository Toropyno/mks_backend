from mks_backend.models.protocol import Protocol
from mks_backend.repositories.meeting import MeetingRepository
from mks_backend.serializers.utils.date_and_time import get_date_string


class ProtocolSerializer:

    def convert_object_to_json(self, protocol: Protocol) -> dict:
        protocol_dict = {
            'protocolId': protocol.protocol_id,
            'protocolNumber': protocol.protocol_num,
            'protocolDate': get_date_string(protocol.protocol_date),
            'meeting': {
                'id': protocol.meetings_type_id,
                'fullName': MeetingRepository.get_meeting_fullname_by_id(protocol.meetings_type_id)  # TODO - fix
            },
            'protocolName': protocol.protocol_name,
            'note': protocol.note,
            'idFileStorage': protocol.idfilestorage
        }
        return protocol_dict

    def convert_list_to_json(self, protocols: list) -> list:
        return list(map(self.convert_object_to_json, protocols))

    def convert_schema_to_object(self, schema_dict: dict) -> Protocol:
        protocol = Protocol()
        if 'id' in schema_dict:
            protocol.protocol_id = schema_dict['id']
        protocol.protocol_num = schema_dict['protocolNumber']
        protocol.protocol_date = schema_dict['protocolDate']
        protocol.meetings_type_id = schema_dict['meeting']
        protocol.protocol_name = schema_dict['protocolName']
        protocol.note = schema_dict['note']
        protocol.idfilestorage = schema_dict['idFileStorage']
        return protocol
