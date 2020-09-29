from sqlalchemy import Column, Integer, VARCHAR, UniqueConstraint

from mks_backend.models import Base


class MeasureUnit(Base):

    __tablename__ = 'measure_units'

    __table_args__ = (
        UniqueConstraint(
            'unit_code',
            'unit_name',
            name='measure_units_unique'
        ),
    )

    unit_id = Column(Integer, primary_key=True)
    unit_code = Column(VARCHAR(20), nullable=False)
    unit_name = Column(VARCHAR(255), nullable=False)
