"""Added grocery, product, store models

Revision ID: b8e32cf2e815
Revises: d15249b99e1d
Create Date: 2024-08-01 16:13:48.475004

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b8e32cf2e815'
down_revision = 'd15249b99e1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', mysql.VARCHAR(length=255), nullable=False))

    # ### end Alembic commands ###
