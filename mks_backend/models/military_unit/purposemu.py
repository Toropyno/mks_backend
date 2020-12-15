from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class PurposeMU(Base):
    __tablename__ = 'purposemu'

    idpurpose = Column(Integer, primary_key=True, autoincrement=True)
    namepurpose = Column(VARCHAR(100), nullable=False)

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='purpose_m_u'
    )
