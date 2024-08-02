"""Updated user model with create date col added

Revision ID: f1eac65a0325
Revises: 760ecfde9bd2
Create Date: 2024-08-02 14:50:04.471676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1eac65a0325'
down_revision = '760ecfde9bd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.create_unique_constraint(None, ['phone'])
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['address'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
