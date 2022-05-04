from sqlalchemy import VARCHAR, Column, Integer
from sqlalchemy.orm import relationship

from mks_backend.db_schemas import ORGANIZATION_SCHEMA
from mks_backend.session import Base


class MilitaryRank(Base):
    """
    Воинские звания
    """
    __tablename__ = 'military_ranks'

    __table_args__ = {'schema': ORGANIZATION_SCHEMA}

    military_ranks_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), nullable=False, unique=True)

    officials = relationship(
        'Official'
    )
