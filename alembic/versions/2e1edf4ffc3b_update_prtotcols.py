"""Update prtotcols

Revision ID: 2e1edf4ffc3b
Revises: aee298720d4f
Create Date: 2021-10-06 11:10:52.398517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e1edf4ffc3b'
down_revision = 'aee298720d4f'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('protocol', sa.Column('signatory', sa.VARCHAR(length=255), nullable=True))
    op.drop_constraint('protocol_idfilestorage_fkey', 'protocol', type_='foreignkey')
    op.create_foreign_key(None, 'protocol', 'filestorage', ['idfilestorage'], ['idfilestorage'], ondelete='SET NULL')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'protocol', type_='foreignkey')
    op.create_foreign_key('protocol_idfilestorage_fkey', 'protocol', 'filestorage', ['idfilestorage'], ['idfilestorage'], ondelete='CASCADE')
    op.drop_column('protocol', 'signatory')
    # ### end Alembic commands ###
