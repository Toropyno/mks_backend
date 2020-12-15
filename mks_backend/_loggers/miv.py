from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    TIMESTAMP
)
from sqlalchemy.dialects.postgresql import UUID

from mks_backend.models import Base, MIV_SCHEMA


class MIVLog(Base):
    __tablename__ = 'miv_logs'
    __table_args__ = {'schema': MIV_SCHEMA}

    id = Column(Integer, primary_key=True)
    type_id = Column(VARCHAR(20), nullable=False)
    description = Column(VARCHAR(1000), nullable=True)
    dt_created = Column(TIMESTAMP, nullable=False)
    message_id = Column(UUID, nullable=True)
