from sqlalchemy import Column, Integer

from mks_backend.models import Base


class Meeting(Base):
    __tablename__ = 'meeting'
    meetings_type_id = Column(Integer, primary_key=True, nullable=False)