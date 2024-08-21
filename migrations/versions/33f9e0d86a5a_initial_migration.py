"""Initial migration.

Revision ID: 33f9e0d86a5a
Revises: 
Create Date: 2024-06-06 02:29:08.764865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33f9e0d86a5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like')
    op.drop_table('comment')
    op.drop_table('user')
    op.drop_table('artwork')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artwork',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('filename', sa.VARCHAR(length=100), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('comment',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('artwork_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['artwork_id'], ['artwork.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('like',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('artwork_id', sa.INTEGER(), nullable=False),
    sa.Column('like_type', sa.BOOLEAN(), nullable=True),
    sa.ForeignKeyConstraint(['artwork_id'], ['artwork.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
