from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.session import Base
from mks_backend.db_schemas import MU_SCHEMA


class PurposeMU(Base):
    __tablename__ = 'purposemu'
    __table_args__ = {'schema': MU_SCHEMA}

    idpurpose = Column(Integer, primary_key=True, autoincrement=True)
    namepurpose = Column(VARCHAR(100), nullable=False)

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='purpose_m_u'
    )
