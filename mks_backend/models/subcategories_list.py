from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.models import Base


class SubcategoriesList(Base):

    __tablename__ = 'subcategories_list'
    subcategories_list_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    construction_categories_id = Column(
        Integer,
        ForeignKey('construction_categories.construction_categories_id', ondelete='CASCADE'))
    construction_subcategories_id = Column(
        Integer,
        ForeignKey('construction_subcategories.construction_subcategories_id', ondelete='CASCADE'))

    construction_category = relationship('ConstructionCategories', back_populates='subcategories_list', passive_deletes=True)
    construction_subcategory = relationship('ConstructionSubcategories', back_populates='subcategories_list', passive_deletes=True)
