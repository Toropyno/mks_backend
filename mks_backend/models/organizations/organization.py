from uuid import uuid4

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    BOOLEAN
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from mks_backend.models import Base, ORGANIZATION_SCHEMA
from mks_backend.models.organizations.organization_history import OrganizationHistory


class Organization(Base):
    """
    Организации
    """

    __tablename__ = 'organizations'

    __table_args__ = {'schema': ORGANIZATION_SCHEMA}

    organizations_id = Column(UUID, primary_key=True, default=uuid4)
    par_number = Column(Integer, nullable=True)
    org_sign = Column(BOOLEAN, default=False, nullable=False)

    parent_organizations_id = Column(
        UUID,
        ForeignKey(organizations_id, ondelete='CASCADE'),
        nullable=True
    )

    # --------- relationships --------- #

    history = relationship(
        'OrganizationHistory',
        order_by='desc(OrganizationHistory.begin_date)',
        back_populates='organization'
    )

    sub_organizations = relationship(
        'Organization',
        cascade='all, delete-orphan',
        passive_deletes=True,
    )

    organization_documents = relationship(
        'OrganizationDocument',
        back_populates='organization'
    )

    parent = relationship(
        'Organization',
        remote_side=organizations_id,
    )

    officials = relationship(
        'Official',
        back_populates='organization'
    )

    # --------- hybrid_properties --------- #

    @hybrid_property
    def children(self) -> list:
        """
        Sorting within the parent is performed by the field "par_number".
        For the same number (or not specified) sorting by the name of a node in the tree.
        """
        return sorted(self.sub_organizations, key=lambda children: (children.par_number, children.shortname))

    @hybrid_property
    def shortname(self) -> str:
        return self.actual.shortname

    @hybrid_property
    def actual(self) -> OrganizationHistory:
        return max(self.history, key=lambda history_record: history_record.begin_date)
