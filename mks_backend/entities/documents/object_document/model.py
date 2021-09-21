from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)

from sqlalchemy.orm import relationship

from mks_backend.session import Base


class ObjectDocument(Base):
    __tablename__ = 'object_documents'

    __table_args__ = (
        UniqueConstraint(
            'construction_objects_id',
            'construction_documents_id',
            name='object_documents_unique'
        ),
    )

    object_documents_id = Column(Integer, primary_key=True, autoincrement=True)

    construction_objects_id = Column(
        Integer,
        ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'),
        nullable=False,
    )

    construction_documents_id = Column(
        Integer,
        ForeignKey('construction_documents.construction_documents_id', ondelete='CASCADE'),
        nullable=False,
    )

    # --------- relationships --------- #

    document = relationship(
        'ConstructionDocument'
    )

    construction_object = relationship(
        'ConstructionObject'
    )
