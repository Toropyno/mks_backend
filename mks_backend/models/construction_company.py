from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    UniqueConstraint,
)

from mks_backend.session import Base


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

    id_fias = Column(Integer)  # TODO: add fias
    address_full = Column(VARCHAR(1000))
    phone = Column(VARCHAR(40))
    email = Column(VARCHAR(80))
    people = Column(Integer)
    equipment = Column(Integer)
    services = Column(VARCHAR(1000))
