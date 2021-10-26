from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
)

from mks_backend.session import Base
from mks_backend.db_schemas import COURTS_SCHEMA


class CourtDecision(Base):
    __tablename__ = 'court_decisions'
    __table_args__ = {'schema': COURTS_SCHEMA}

    court_decisions_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), nullable=False, unique=True, comment='Полное название')
