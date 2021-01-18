from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class MilitaryCity(Base):
    __tablename__ = 'militarycity'

    idmilitarycity = Column(Integer, primary_key=True, autoincrement=True)
    namemilitarycity = Column(VARCHAR(50), nullable=False)

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='military_city'
    )
