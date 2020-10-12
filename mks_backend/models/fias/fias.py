from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from sqlalchemy.orm import relationship

from mks_backend.models import Base


class FIAS(Base):
    __tablename__ = 'fias'

    id = Column(Integer, primary_key=True)

    subject_id = Column(
        Integer,
        ForeignKey('subject.id')
    )

    district_id = Column(
        Integer,
        ForeignKey('district.id')
    )

    city_id = Column(
        Integer,
        ForeignKey('city.id')
    )

    locality_id = Column(
        Integer,
        ForeignKey('locality.id')
    )

    remaining_address_id = Column(
        Integer,
        ForeignKey('remaining_address.id', ondelete='SET NULL')
    )

    subject = relationship(
        'Subject',
        back_populates='fiases'
    )

    district = relationship(
        'District',
        back_populates='fiases'
    )

    city = relationship(
        'City',
        back_populates='fiases'
    )

    locality = relationship(
        'Locality',
        back_populates='fiases'
    )

    remaining_address = relationship(
        'RemainingAddress',
        back_populates='fias'
    )
