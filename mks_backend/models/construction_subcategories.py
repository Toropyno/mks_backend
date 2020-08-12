from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.models import Base


class ConstructionSubcategories(Base):

    __tablename__ = 'construction_subcategories'
    construction_subcategories_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)

    subcategories_list = relationship('SubcategoriesList', back_populates='construction_subcategories')
