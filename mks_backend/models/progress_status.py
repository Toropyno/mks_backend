from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)

from mks_backend.models import Base


class ProgressStatus(Base):

    __tablename__ = 'progress_statuses'
    progress_statuses_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
