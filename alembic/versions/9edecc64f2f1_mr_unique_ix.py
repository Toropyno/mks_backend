"""mr_unique_ix

Revision ID: 9edecc64f2f1
Revises: 9f8c08bdaa01
Create Date: 2022-05-04 12:13:01.377093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9edecc64f2f1'
down_revision = '9f8c08bdaa01'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'military_ranks', ['fullname'], schema='organization')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'military_ranks', schema='organization', type_='unique')
    # ### end Alembic commands ###
