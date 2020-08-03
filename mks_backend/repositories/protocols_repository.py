from mks_backend.models.protocol import Protocol
from mks_backend.repositories import DBSession


class ProtocolRepository(object):
    def get_all_protocols(self):
        return DBSession.query(Protocol)

    def get_protocol_by_id(self, id):
        return DBSession.query(Protocol).get(id)

    def add_protocol(self, protocol):
        DBSession.add(protocol)
        DBSession.commit()

    def delete_protocol_by_id(self, id):
        protocol = self.get_protocol_by_id(id)
        DBSession.delete(protocol)
        DBSession.commit()

    def update_protocol(self, protocol):
        DBSession.query(Protocol).filter_by(protocol_id=protocol.protocol_id).update(
            {'protocol_num': protocol.protocol_num,
             'protocol_date': protocol.protocol_date,
             'meetings_type_id': protocol.meetings_type_id,
             'protocol_name': protocol.protocol_name,
             'note': protocol.note})
        DBSession.commit()

    def filter_protocols(self, protocols, params):
        meetings_type_id = params.get('meetingsTypeId')
        protocol_name = params.get('protocolName')
        protocol_num = params.get('protocolNumber')
        date_start = params.get('dateStart')
        date_end = params.get('dateEnd')

        if meetings_type_id:
            protocols = protocols.filter_by(meetings_type_id=meetings_type_id)
        if protocol_name:
            protocol_name = "%" + protocol_name + "%"
            protocols = protocols.filter(Protocol.protocol_name.like(protocol_name))
        if protocol_num:
            protocol_num = "%" + protocol_num + "%"
            protocols = protocols.filter(Protocol.protocol_num.like(protocol_num))
        if date_start and date_end:
            protocols = protocols.filter(Protocol.protocol_date >= date_start, Protocol.protocol_date <= date_end)
        return protocols.all()
