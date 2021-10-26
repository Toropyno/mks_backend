from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)

from mks_backend.session import Base
from mks_backend.db_schemas import COURTS_SCHEMA


class Courts(Base):
    __tablename__ = 'courts'
    __table_args__ = {'schema': COURTS_SCHEMA}

    courts_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
