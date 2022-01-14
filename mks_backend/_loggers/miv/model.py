from sqlalchemy import TIMESTAMP, VARCHAR, Column, Integer
from sqlalchemy.dialects.postgresql import UUID

from mks_backend.db_schemas import MIV_SCHEMA
from mks_backend.session import Base


class MIVLog(Base):
    __tablename__ = 'miv_logs'
    __table_args__ = {'schema': MIV_SCHEMA}

    id = Column(Integer, primary_key=True)
    type_id = Column(VARCHAR(20), nullable=False)
    description = Column(VARCHAR(1000), nullable=True)
    dt_created = Column(TIMESTAMP, nullable=False)
    message_id = Column(UUID, nullable=True)
