from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class Meeting(Base):
    __tablename__ = 'meeting'

    meetings_type_id = Column(Integer, primary_key=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
