from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class ProgressStatus(Base):
    __tablename__ = 'progress_statuses'

    progress_statuses_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    construction_progress = relationship(
        'ConstructionProgress',
        back_populates='progress_status'
    )
