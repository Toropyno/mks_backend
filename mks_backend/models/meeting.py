from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class Meetings_type(Base):
    __tablename__ = 'meeting'
    meetings_type_id = Column(Integer, primary_key=True, nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)

    protocols = relationship("Protocol", back_populates="meeting")
