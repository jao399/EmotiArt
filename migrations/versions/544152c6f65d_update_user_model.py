"""Update User model

Revision ID: 544152c6f65d
Revises: 33f9e0d86a5a
Create Date: 2024-06-06 04:43:46.835232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '544152c6f65d'
down_revision = '33f9e0d86a5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hashed_password', sa.String(length=128), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
        batch_op.drop_column('hashed_password')

    # ### end Alembic commands ###
