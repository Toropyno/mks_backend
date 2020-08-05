from mks_backend.repositories.meeting_repository import MeetingRepository

from ..models.protocol import Protocol

class ProtocolSerializer(object):
    def convert_object_to_json(self, protocol):
        protocol_dict = {
            'protocolId': protocol.protocol_id,
            'protocolNumber': protocol.protocol_num,
            'protocolDate': self.get_date_string(protocol.protocol_date),
            'meeting': {
                'id': protocol.meetings_type_id,
                'fullName': MeetingRepository.get_meeting_fullname_by_id(protocol.meetings_type_id)
            },
            'protocolName': protocol.protocol_name,
            'note': protocol.note,
            'idFileStorage': protocol.idfilestorage
        }
        return protocol_dict

    def get_date_string(self, date):
        return str(date.day) + '.' + str(date.month) + '.' + str(date.year)

    def convert_list_to_json(self, protocols):
        protocols_array = []

        for protocol in protocols:
            protocol_dict = self.convert_object_to_json(protocol)
            protocols_array.append(protocol_dict)

        return protocols_array

    def convert_schema_to_object(self, schema_dict):
        protocol = Protocol()
        if 'id' in schema_dict:
            protocol.protocol_id = schema_dict['id']
        protocol.protocol_num = schema_dict['protocolNumber']
        protocol.protocol_date = schema_dict['protocolDate']
        protocol.meetings_type_id = schema_dict['meeting']
        protocol.protocol_name = schema_dict['protocolName']
        protocol.note = schema_dict['note']
        #protocol.idfilestorage = schema_dict['idFileStorage']
        return protocol


    def get_params_from_schema(self,schema_dict):
        date_start = schema_dict['dateStart'] if 'dateStart' in schema_dict else None
        date_end = schema_dict['dateEnd'] if 'dateEnd' in schema_dict else None
        protocol_num = schema_dict['protocolNumber'] if 'protocolNumber' in schema_dict else None
        meetings_type_id = schema_dict['meeting'] if 'meeting' in schema_dict else None
        protocol_name = schema_dict['protocolName'] if 'protocolName' in schema_dict else None

        params = {}

        if date_start is not None:
            params['dateStart'] = date_start
        if date_end is not None:
            params['dateEnd'] = date_end
        if protocol_num is not None:
            params['protocolNumber'] = protocol_num
        if protocol_name is not None:
            params['protocolName'] = protocol_name
        if meetings_type_id is not None:
            params['meeting'] = meetings_type_id

        return params

