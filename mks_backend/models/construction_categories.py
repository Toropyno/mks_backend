from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class ConstructionCategories(Base):

    __tablename__ = 'construction_categories'
    construction_categories_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)

    subcategories_list = relationship('SubcategoriesList', back_populates='construction_category')
