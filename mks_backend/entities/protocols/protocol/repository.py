from .model import Protocol
from mks_backend.session import DBSession

from mks_backend.errors import DBBasicError


class ProtocolRepository:

    def __init__(self):
        self._query = DBSession.query(Protocol)

    def get_protocol_by_id(self, id_: int) -> Protocol:
        protocol = self._query.get(id_)
        if not protocol:
            raise DBBasicError('protocol_ad')
        return protocol

    def get_all_protocols(self) -> list:
        return self._query.order_by(Protocol.protocol_date.desc()).all()

    def add_protocol(self, protocol: Protocol) -> None:
        DBSession.add(protocol)
        DBSession.commit()

    def delete_protocol_by_id(self, id_: int) -> None:
        protocol = self.get_protocol_by_id(id_)
        DBSession.delete(protocol)
        DBSession.commit()

    def update_protocol(self, protocol: Protocol) -> None:
        self._query.filter_by(protocol_id=protocol.protocol_id).update(
            {
                'protocol_num': protocol.protocol_num,
                'protocol_date': protocol.protocol_date,
                'meetings_type_id': protocol.meetings_type_id,
                'protocol_name': protocol.protocol_name,
                'note': protocol.note,
                'idfilestorage': protocol.idfilestorage,
                'signatory': protocol.signatory
            }
        )
        DBSession.commit()

    def filter_protocols(self, params: dict) -> list:
        meetings_type_id = params.get('meeting')
        protocol_name = params.get('protocol_name')
        protocol_num = params.get('protocol_number')
        date_start = params.get('date_start')
        date_end = params.get('date_end')
        signatory = params.get('signatory')

        protocols = self._query

        if meetings_type_id:
            protocols = protocols.filter(Protocol.meetings_type_id == meetings_type_id)
        if protocol_name:
            protocol_name = '%' + protocol_name + '%'
            protocols = protocols.filter(Protocol.protocol_name.ilike(protocol_name))
        if protocol_num:
            protocol_num = '%' + protocol_num + '%'
            protocols = protocols.filter(Protocol.protocol_num.ilike(protocol_num))
        if date_start:
            protocols = protocols.filter(Protocol.protocol_date >= date_start)
        if date_end:
            protocols = protocols.filter(Protocol.protocol_date <= date_end)
        if signatory:
            protocols = protocols.filter(Protocol.signatory == signatory)

        return protocols.order_by(Protocol.protocol_date.desc()).all()
