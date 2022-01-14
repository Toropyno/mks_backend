from sqlalchemy import VARCHAR, Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

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

    address_full = Column(VARCHAR(1000))
    phone = Column(VARCHAR(40))
    email = Column(VARCHAR(80))
    people = Column(Integer)
    equipment = Column(Integer)
    services = Column(VARCHAR(1000))

    id_fias = Column(
        Integer,
        ForeignKey('fias.id', ondelete='SET NULL')
    )

    fias = relationship('FIAS')
