from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, UUID, VARCHAR

from mks_backend.session import Base


class FIAS(Base):
    __tablename__ = 'fias'

    id = Column(INTEGER, primary_key=True)
    aoid = Column(UUID(as_uuid=True), unique=True, nullable=False)
    region = Column(VARCHAR(64), comment='субъект РФ')
    area = Column(VARCHAR(64), comment='район')
    city = Column(VARCHAR(64), comment='город')
    settlement = Column(VARCHAR(64), comment='населенный пункт')
    street = Column(VARCHAR(64), comment='улица')
    home = Column(VARCHAR(64), comment='дом')
    body = Column(VARCHAR(64), comment='корпус')
    structure = Column(VARCHAR(64), comment='строение')

    def __json__(self, *args):
        return {
            'aoid': str(self.aoid),
            'region': self.region,
            'street': self.street,
            'area': self.area,
            'city': self.city,
            'settlement': self.settlement
        }
