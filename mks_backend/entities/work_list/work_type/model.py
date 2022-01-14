from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.session import Base


class WorkType(Base):
    __tablename__ = 'work_types'

    work_types_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
    note = Column(VARCHAR(1000), nullable=True)
