"""add creator flag to mazes

Revision ID: 09c0ba93f05a
Revises: a3dfa5ea0bda
Create Date: 2023-10-24 15:51:03.468861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09c0ba93f05a'
down_revision = 'a3dfa5ea0bda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mazes', sa.Column('creator', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mazes', 'creator')
    # ### end Alembic commands ###
