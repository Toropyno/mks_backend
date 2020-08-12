from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.models import Base


class ConstructionCategories(Base):

    __tablename__ = 'construction_categories'
    construction_categories_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)

    construction_subcategories = relationship("SubcategoriesList", back_populates='construction_categories')
