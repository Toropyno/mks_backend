from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from mks_backend.models import Base


class ObjectCategoriesList(Base):

    __tablename__ = 'object_categories_list'
    object_categories_list_id = Column(Integer, primary_key=True, autoincrement=True)
    zones_id = Column(Integer, ForeignKey('zones.zones_id', ondelete='CASCADE'), unique=True, nullable=False)
    object_categories_id = Column(Integer, ForeignKey('object_categories.object_categories_id', ondelete='CASCADE'),
                                  unique=True, nullable=False)

    zone = relationship(
        'Zones',
        back_populates='object_categories_list'
    )

    object_categories_instance = relationship(
        'ObjectCategories',
        back_populates='object_categories_list'
    )

    construction_object = relationship(
        'ConstructionObjects',
        back_populates='object_categories_list'
    )
