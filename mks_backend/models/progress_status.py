from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class ProgressStatus(Base):

    __tablename__ = 'progress_statuses'
    progress_statuses_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

<<<<<<< HEAD
    # construction_progress = relationship(
    #     'ConstructionProgress',
    #     back_populates='progress_statuses'
    # )
=======
    construction_progress = relationship(
        'ConstructionProgress',
        back_populates='progress_statuses'
    )
>>>>>>> fd0aeb659d04334ca91a033b2ab22c5097dd060d
