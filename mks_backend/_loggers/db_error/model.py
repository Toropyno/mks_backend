from sqlalchemy import TIMESTAMP, VARCHAR, Column, Integer
from sqlalchemy.sql import func

from mks_backend.db_schemas import LOG_SCHEMA
from mks_backend.session import Base


class DBError(Base):
    __tablename__ = 'db_error'
    __table_args__ = {'schema': LOG_SCHEMA}

    id = Column(Integer, primary_key=True)
    time = Column(TIMESTAMP, default=func.now())
    error_raw = Column(VARCHAR(512))

    def __json__(self, *args):
        return {
            'id': self.id,
            'time': self.time.strftime('%d.%m.%Y %H:%M:%S'),
            'error_raw': self.error_raw
        }
