class ProtocolSerializer(object):

    def convert_object_to_json(self, protocol):
        protocol_dict = {
            "protocolId": protocol.protocol_id,
            "protocolNumber": protocol.protocol_num,
            "protocolDate": str(protocol.protocol_date),
            "meetingsTypeId": protocol.meetings_type_id,
            "protocolName": protocol.protocol_name,
            "note": protocol.note,
            "idFileStorage": protocol.idfilestorage}
        return protocol_dict

    def convert_list_to_json(self, protocols):
        protocols_array = []

        for protocol in protocols:
            protocol_dict = self.convert_object_to_json(protocol)
            protocols_array.append(protocol_dict)

        return protocols_array
