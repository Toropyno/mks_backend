from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    UniqueConstraint,
)

from mks_backend.models import Base


class ConstructionCompany(Base):

    __tablename__ = 'construction_companies'

    __table_args__ = (
        UniqueConstraint(
            'shortname',
            'fullname',
            name='construction_companies_unique'
        ),
    )

    construction_companies_id = Column(Integer, primary_key=True)
    shortname = Column(VARCHAR(100), nullable=False)
    fullname = Column(VARCHAR(1000), nullable=False)
