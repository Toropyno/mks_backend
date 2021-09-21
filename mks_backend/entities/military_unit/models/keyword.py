from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.session import Base
from mks_backend.db_schemas import MU_SCHEMA


class Keyword(Base):
    __tablename__ = 'keyword'
    __table_args__ = {'schema': MU_SCHEMA}

    idkeyword = Column(Integer, primary_key=True, autoincrement=True)
    namekeyword = Column(VARCHAR(50), nullable=False)

    name_military_unit = relationship(
        'NameMilitaryUnit',
        back_populates='keyword',
        passive_deletes=True
    )
