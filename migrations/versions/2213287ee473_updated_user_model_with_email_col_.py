"""Updated user model with email col removed

Revision ID: 2213287ee473
Revises: f1eac65a0325
Create Date: 2024-08-02 14:52:06.170375

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2213287ee473'
down_revision = 'f1eac65a0325'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['address'])
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
