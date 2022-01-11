from .model import Protocol

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.protocols.meeting import MeetingSerializer
from mks_backend.entities.filestorage import FileStorageSerializer
from mks_backend.utils.date_and_time import get_date_string

from mks_backend.errors import serialize_error_handler


class ProtocolSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, protocol: Protocol) -> dict:
        return {
            'protocolId': protocol.protocol_id,
            'protocolNumber': protocol.protocol_num,
            'protocolDate': get_date_string(protocol.protocol_date),
            'meeting': MeetingSerializer.to_json(
                protocol.meeting
            ),
            'protocolName': protocol.protocol_name,
            'note': protocol.note,
            'protocolFile': FileStorageSerializer.to_json(
                protocol.filestorage
            ),
            'signatory': protocol.signatory
        }

    def to_mapped_object(self, schema_dict: dict) -> Protocol:
        protocol = Protocol()

        protocol.protocol_id = schema_dict.get('id')
        protocol.protocol_num = schema_dict.get('protocolNumber')
        protocol.protocol_date = schema_dict.get('protocolDate')
        protocol.meetings_type_id = schema_dict.get('meeting')
        protocol.protocol_name = schema_dict.get('protocolName')
        protocol.note = schema_dict.get('note')
        protocol.idfilestorage = schema_dict.get('idFileStorage')
        protocol.signatory = schema_dict.get('signatory')

        return protocol
