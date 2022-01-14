from sqlalchemy import VARCHAR, Column, Date, ForeignKey, Integer, PrimaryKeyConstraint
from sqlalchemy.sql import func

from mks_backend.db_schemas import MU_SCHEMA
from mks_backend.session import Base


class MilitaryUnitExtension(Base):
    __tablename__ = 'MilitaryUnit_extension'
    __table_args__ = (
        PrimaryKeyConstraint(
            'idMU',
            'start_date',
            name='military_unit_extension_pk'
        ),
        {'schema': MU_SCHEMA})

    report_name = Column(VARCHAR(255), nullable=False)
    start_date = Column(Date(), nullable=False, default=func.current_date())

    idMU = Column(
        Integer,
        ForeignKey('{schema}.military_unit.idMU'.format(schema=MU_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )
