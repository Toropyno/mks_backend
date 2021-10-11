from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.session import Base


class CriticalCategory(Base):
    __tablename__ = 'critical_categories'

    critical_categories_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
