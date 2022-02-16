from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.db_schemas import COURTS_SCHEMA
from mks_backend.session import Base


class ParticipantStatus(Base):
    __tablename__ = 'participant_statuses'
    __table_args__ = {'schema': COURTS_SCHEMA}

    participant_statuses_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
