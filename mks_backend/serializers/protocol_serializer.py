class ProtocolSerializer(object):

    def convert_object_to_json(self, protocol):
        protocol_dict = {
            "protocolId": protocol.protocol_id,
            "protocolNumber": protocol.protocol_num,
            "protocolDate": self.get_date_string(protocol.protocol_date),
            "meetingsTypeId": protocol.meetings_type_id,
            "protocolName": protocol.protocol_name,
            "note": protocol.note,
            "idFileStorage": protocol.idfilestorage}
        return protocol_dict

    def get_date_string(self, date):
        return str(date.day) + '.' + str(date.month) + '.' + str(date.year)

    def convert_list_to_json(self, protocols):
        protocols_array = []

        for protocol in protocols:
            protocol_dict = self.convert_object_to_json(protocol)
            protocols_array.append(protocol_dict)

        return protocols_array
