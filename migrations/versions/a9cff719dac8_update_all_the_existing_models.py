"""Update all the existing models

Revision ID: a9cff719dac8
Revises: 1a732bf693cd
Create Date: 2024-08-08 21:04:14.214619

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a9cff719dac8'
down_revision = '1a732bf693cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('type', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('store_product_mapping',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('expiry_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_grocery_name')
    with op.batch_alter_table('grocery_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('grocery_name_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('item_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key(None, 'product', ['item_id'], ['id'])
        batch_op.create_foreign_key(None, 'grocery_name', ['grocery_name_id'], ['id'])
        batch_op.drop_column('product_type')
        batch_op.drop_column('price')
        batch_op.drop_column('expiry_date')
        batch_op.drop_column('name')

    with op.batch_alter_table('grocery_name', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(None, ['type'])
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('last_login', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('modified_at', sa.DateTime(), nullable=True))
        batch_op.drop_index('address')
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('address', ['address'], unique=True)
        batch_op.drop_column('modified_at')
        batch_op.drop_column('last_login')
        batch_op.drop_column('email')

    with op.batch_alter_table('grocery_name', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('user_id')
        batch_op.drop_column('is_active')
        batch_op.drop_column('modified_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('type')

    with op.batch_alter_table('grocery_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', mysql.VARCHAR(length=80), nullable=False))
        batch_op.add_column(sa.Column('expiry_date', sa.DATE(), nullable=False))
        batch_op.add_column(sa.Column('price', mysql.FLOAT(), nullable=False))
        batch_op.add_column(sa.Column('product_type', mysql.VARCHAR(length=80), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('modified_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('item_id')
        batch_op.drop_column('grocery_name_id')

    op.create_table('user_grocery_name',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('grocery_name_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['grocery_name_id'], ['grocery_name.id'], name='user_grocery_name_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_grocery_name_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('store_product_mapping')
    op.drop_table('store')
    op.drop_table('product')
    # ### end Alembic commands ###