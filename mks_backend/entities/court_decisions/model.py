from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.db_schemas import COURTS_SCHEMA
from mks_backend.session import Base


class CourtDecision(Base):
    __tablename__ = 'court_decisions'
    __table_args__ = {'schema': COURTS_SCHEMA}

    court_decisions_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), nullable=False, unique=True, comment='Полное название')
