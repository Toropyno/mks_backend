from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class NameMilitaryUnit(Base):

    __tablename__ = 'namemilitaryunit'

    idnamemu = Column(Integer, primary_key=True, autoincrement=True)
    namemu = Column(VARCHAR(250), nullable=False)
    snamemu = Column(VARCHAR(20))

    idkeyword = Column(
        Integer,
        ForeignKey('keyword.idkeyword', ondelete='CASCADE'),
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
