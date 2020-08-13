from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.models import Base


class MeetingsType(Base):

    __tablename__ = 'meeting'
    meetings_type_id = Column(Integer, primary_key=True, nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)
