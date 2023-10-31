"""add isTest flag

Revision ID: 186b1d182e84
Revises: 81b898b28700
Create Date: 2023-10-10 14:19:43.378971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '186b1d182e84'
down_revision = '81b898b28700'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mazes', sa.Column('isTest', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mazes', 'isTest')
    # ### end Alembic commands ###