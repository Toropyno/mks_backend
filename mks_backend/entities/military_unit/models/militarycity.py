from sqlalchemy import VARCHAR, Column, Integer
from sqlalchemy.orm import relationship

from mks_backend.db_schemas import MU_SCHEMA
from mks_backend.session import Base


class MilitaryCity(Base):
    __tablename__ = 'militarycity'
    __table_args__ = {'schema': MU_SCHEMA}

    idmilitarycity = Column(Integer, primary_key=True, autoincrement=True)
    namemilitarycity = Column(VARCHAR(50), nullable=False)

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='military_city'
    )
