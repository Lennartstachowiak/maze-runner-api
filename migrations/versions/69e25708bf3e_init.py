"""init

Revision ID: 69e25708bf3e
Revises: 
Create Date: 2024-04-24 17:50:13.350244

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "69e25708bf3e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("username", sa.String(length=32), nullable=True),
        sa.Column("email", sa.String(length=32), nullable=True),
        sa.Column("password", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "algorithms",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("code", sa.Text(), nullable=False),
        sa.Column("user_id", sa.String(length=32), nullable=False),
        sa.Column("is_working", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    with op.batch_alter_table("algorithms", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_algorithms_user_id"), ["user_id"], unique=False)

    op.create_table(
        "mazes",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("difficulty", sa.Enum("Easy", "Medium", "Hard", name="difficulty"), nullable=False),
        sa.Column("img_link", sa.Text(), nullable=False),
        sa.Column("structure", sa.Text(), nullable=False),
        sa.Column("height", sa.Integer(), nullable=False),
        sa.Column("width", sa.Integer(), nullable=False),
        sa.Column("is_test", sa.Boolean(), nullable=True),
        sa.Column("creator", sa.String(length=32), nullable=False),
        sa.ForeignKeyConstraint(
            ["creator"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    with op.batch_alter_table("mazes", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_mazes_creator"), ["creator"], unique=False)

    op.create_table(
        "sessions",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("user_id", sa.String(length=32), nullable=False),
        sa.Column("expiry_date", sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    with op.batch_alter_table("sessions", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_sessions_user_id"), ["user_id"], unique=True)

    op.create_table(
        "user_followers",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("user_id", sa.String(length=32), nullable=False),
        sa.Column("follower_id", sa.String(length=32), nullable=False),
        sa.CheckConstraint("user_id!=follower_id", name="_user_follower_check_"),
        sa.ForeignKeyConstraint(
            ["follower_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("user_id", "follower_id", name="_user_follower_uc"),
    )
    with op.batch_alter_table("user_followers", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_user_followers_follower_id"), ["follower_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_user_followers_user_id"), ["user_id"], unique=False)

    op.create_table(
        "highscores",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("user_id", sa.String(length=32), nullable=False),
        sa.Column("maze_id", sa.String(length=32), nullable=False),
        sa.Column("algorithm_id", sa.String(length=32), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["algorithm_id"],
            ["algorithms.id"],
        ),
        sa.ForeignKeyConstraint(
            ["maze_id"],
            ["mazes.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    with op.batch_alter_table("highscores", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_highscores_algorithm_id"), ["algorithm_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_highscores_maze_id"), ["maze_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_highscores_user_id"), ["user_id"], unique=False)

    op.create_table(
        "maze_followers",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("maze_id", sa.String(length=32), nullable=False),
        sa.Column("follower_id", sa.String(length=32), nullable=False),
        sa.ForeignKeyConstraint(
            ["follower_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["maze_id"],
            ["mazes.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("maze_id", "follower_id", name="_maze_follower_uc"),
    )
    with op.batch_alter_table("maze_followers", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_maze_followers_follower_id"), ["follower_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_maze_followers_maze_id"), ["maze_id"], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("maze_followers", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_maze_followers_maze_id"))
        batch_op.drop_index(batch_op.f("ix_maze_followers_follower_id"))

    op.drop_table("maze_followers")
    with op.batch_alter_table("highscores", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_highscores_user_id"))
        batch_op.drop_index(batch_op.f("ix_highscores_maze_id"))
        batch_op.drop_index(batch_op.f("ix_highscores_algorithm_id"))

    op.drop_table("highscores")
    with op.batch_alter_table("user_followers", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_user_followers_user_id"))
        batch_op.drop_index(batch_op.f("ix_user_followers_follower_id"))

    op.drop_table("user_followers")
    with op.batch_alter_table("sessions", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_sessions_user_id"))

    op.drop_table("sessions")
    with op.batch_alter_table("mazes", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_mazes_creator"))

    op.drop_table("mazes")
    with op.batch_alter_table("algorithms", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_algorithms_user_id"))

    op.drop_table("algorithms")
    op.drop_table("users")
    # ### end Alembic commands ###