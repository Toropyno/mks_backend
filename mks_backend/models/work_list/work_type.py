from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.models import Base


class WorkType(Base):

    __tablename__ = 'work_types'

    work_types_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
    note = Column(VARCHAR(1000), nullable=True)