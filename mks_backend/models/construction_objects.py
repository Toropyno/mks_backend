from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    ForeignKey,
    Date,
    DECIMAL,
    CheckConstraint,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from mks_backend.models import Base


class ConstructionObjects(Base):

    __tablename__ = 'construction_objects'
    construction_objects_id = Column(Integer, primary_key=True, autoincrement=True)
    construction_id = Column(Integer, ForeignKey('construction.construction_id', ondelete='CASCADE'), nullable=False)
    object_code = Column(VARCHAR(40), unique=True, nullable=False)
    object_name = Column(VARCHAR(255), nullable=False)
    zones_id = Column(Integer, ForeignKey('zones.zones_id'))
    object_categories_list_id = Column(Integer, ForeignKey('object_categories_list.object_categories_list_id'))
    planned_date = Column(Date, default=func.current_date(), nullable=False)
    weight = Column(Integer, CheckConstraint('weight>0 AND weight<=100'), nullable=False)
    generalplan_number = Column(Integer)
    building_volume = Column(DECIMAL(17, 3))
    floors_amount = Column(Integer)
    construction_stages_id = Column(Integer, ForeignKey('construction_stages.construction_stages_id',
                                                        ondelete='CASCADE'))

    construction = relationship(
        'Construction',
        back_populates='construction_objects'
    )

    zone = relationship(
        'Zone',
        back_populates='construction_object'
    )

    object_categories_list = relationship(
        'ObjectCategoriesList',
        back_populates='construction_object'
    )

    construction_stage = relationship(
        'ConstructionStages',
        back_populates='construction_object'
    )
