"""Add column size to user model

Revision ID: d15249b99e1d
Revises: a03bc1690d2c
Create Date: 2024-07-26 18:11:34.394902

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd15249b99e1d'
down_revision = 'a03bc1690d2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=64),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=128),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=64),
               existing_nullable=False)

    # ### end Alembic commands ###