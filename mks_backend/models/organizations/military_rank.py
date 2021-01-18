from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)

from mks_backend.session import Base
from mks_backend.db_schemas import ORGANIZATION_SCHEMA
from sqlalchemy.orm import relationship


class MilitaryRank(Base):
    __tablename__ = 'military_ranks'

    __table_args__ = {'schema': ORGANIZATION_SCHEMA}

    military_ranks_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), nullable=False)

    officials = relationship(
        'Official'
    )
