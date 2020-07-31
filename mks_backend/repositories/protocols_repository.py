from mks_backend.models.protocol import Protocol
from mks_backend.repositories import DBSession


class ProtocolRepository(object):

    def get_all_protocols(self):
        return DBSession.query(Protocol).all()

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
        DBSession.query(Protocol).get(protocol.protocol_id).update(
            {'protocol_num': protocol.protocol_num,
             'protocol_date': protocol.protocol_date,
             'meetings_type_id': protocol.meetings_type_id,
             'protocol_name': protocol.protocol_name,
             'note': protocol.note})
        DBSession.commit()

