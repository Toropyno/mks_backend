from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)

from mks_backend.models import Base, ORGANIZATION_SCHEMA


class MilitaryRank(Base):

    __tablename__ = 'military_ranks'

    __table_args__ = {'schema': ORGANIZATION_SCHEMA}

    military_ranks_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
