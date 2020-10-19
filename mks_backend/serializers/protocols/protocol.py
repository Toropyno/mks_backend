from mks_backend.models.protocols.protocol import Protocol
from mks_backend.serializers.protocols.meeting import MeetingSerializer
from mks_backend.serializers.utils.date_and_time import get_date_string

from mks_backend.errors.serilize_error import serialize_error_handler


class ProtocolSerializer:

    def convert_list_to_json(self, protocols: list) -> list:
        return list(map(self.convert_object_to_json, protocols))

    def convert_object_to_json(self, protocol: Protocol) -> dict:
        return {
            'protocolId': protocol.protocol_id,
            'protocolNumber': protocol.protocol_num,
            'protocolDate': get_date_string(protocol.protocol_date),
            'meeting': MeetingSerializer.convert_object_to_json(
                protocol.meeting
            ),
            'protocolName': protocol.protocol_name,
            'note': protocol.note,
            'idFileStorage': protocol.idfilestorage
        }

    @classmethod
    @serialize_error_handler
    def to_short_json(cls, protocol: Protocol):
        return {
            'protocolId': protocol.protocol_id,
            'protocolName': protocol.protocol_name,
            'protocolNumber': protocol.protocol_num,
            'protocolDate': get_date_string(protocol.protocol_date),
        }

    def convert_schema_to_object(self, schema_dict: dict) -> Protocol:
        protocol = Protocol()

        protocol.protocol_id = schema_dict.get('id')
        protocol.protocol_num = schema_dict.get('protocolNumber')
        protocol.protocol_date = schema_dict.get('protocolDate')
        protocol.meetings_type_id = schema_dict.get('meeting')
        protocol.protocol_name = schema_dict.get('protocolName')
        protocol.note = schema_dict.get('note')
        protocol.idfilestorage = schema_dict.get('idFileStorage')

        return protocol
