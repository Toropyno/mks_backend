from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    CHAR
)

from mks_backend.models import Base


class OKSM(Base):

    __tablename__ = 'OKSM'
    oksm_id = Column(Integer, primary_key=True)
    code = Column(CHAR(3), unique=True, nullable=False)
    shortname = Column(VARCHAR(80), unique=True, nullable=False)
    fullname = Column(VARCHAR(255))
    alpha2 = Column(CHAR(2), unique=True, nullable=False)
    alpha3 = Column(CHAR(3), unique=True, nullable=False)
