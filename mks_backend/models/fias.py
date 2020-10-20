from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.models import Base


class FIAS(Base):

    __tablename__ = 'fias'

    id = Column(Integer, primary_key=True)
    subject = Column(VARCHAR(100))
    district = Column(VARCHAR(100))
    city = Column(VARCHAR(100))
    locality = Column(VARCHAR(100))
    remaining_address = Column(VARCHAR(100))
