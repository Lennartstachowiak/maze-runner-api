"""add algorithm id to highscore

Revision ID: c35b303a2927
Revises: be2b80773ff7
Create Date: 2023-11-06 16:14:22.003937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c35b303a2927'
down_revision = 'be2b80773ff7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'algorithms', ['id'])
    op.add_column('highscores', sa.Column('algorithm_id', sa.String(length=32), nullable=False))
    op.create_unique_constraint(None, 'highscores', ['id'])
    op.create_foreign_key(None, 'highscores', 'algorithms', ['algorithm_id'], ['id'])
    op.create_unique_constraint(None, 'mazes', ['id'])
    op.create_unique_constraint(None, 'sessions', ['id'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'sessions', type_='unique')
    op.drop_constraint(None, 'mazes', type_='unique')
    op.drop_constraint(None, 'highscores', type_='foreignkey')
    op.drop_constraint(None, 'highscores', type_='unique')
    op.drop_column('highscores', 'algorithm_id')
    op.drop_constraint(None, 'algorithms', type_='unique')
    # ### end Alembic commands ###