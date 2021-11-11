"""Added account table

Revision ID: beb9eec5205b
Revises: 
Create Date: 2021-11-11 14:21:39.024998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beb9eec5205b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goodsStatus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ordersStatus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=45), nullable=True),
    sa.Column('category', sa.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userStatus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=45), nullable=True),
    sa.Column('isAvailable', sa.Boolean(), nullable=True),
    sa.Column('photoURL', sa.VARCHAR(length=45), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('goodsStatus_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goodsStatus_id'], ['goodsStatus.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=45), nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=45), nullable=True),
    sa.Column('lastname', sa.VARCHAR(length=45), nullable=True),
    sa.Column('email', sa.VARCHAR(length=45), nullable=True),
    sa.Column('password', sa.VARCHAR(length=300), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=45), nullable=True),
    sa.Column('userStatus_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userStatus_id'], ['userStatus.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shipDate', sa.DateTime(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.Column('ordersStatus_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('goods_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goods_id'], ['goods.id'], ),
    sa.ForeignKeyConstraint(['ordersStatus_id'], ['ordersStatus.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('user')
    op.drop_table('goods')
    op.drop_table('userStatus')
    op.drop_table('store')
    op.drop_table('ordersStatus')
    op.drop_table('goodsStatus')
    # ### end Alembic commands ###