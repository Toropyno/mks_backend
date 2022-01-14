from sqlalchemy import VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from mks_backend.db_schemas import MU_SCHEMA
from mks_backend.session import Base


class NameMilitaryUnit(Base):
    __tablename__ = 'namemilitaryunit'
    __table_args__ = {'schema': MU_SCHEMA}

    idnamemu = Column(Integer, primary_key=True, autoincrement=True)
    namemu = Column(VARCHAR(250), nullable=False)
    snamemu = Column(VARCHAR(20))

    idkeyword = Column(
        Integer,
        ForeignKey('{schema}.keyword.idkeyword'.format(schema=MU_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    # --------- relationships --------- #

    keyword = relationship(
        'Keyword',
        back_populates='name_military_unit'
    )

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='name_military_unit'
    )
