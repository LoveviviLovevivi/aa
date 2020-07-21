"""empty message

Revision ID: 4d7522fe38eb
Revises: 90b2b05c29de
Create Date: 2020-06-08 14:37:41.021476

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4d7522fe38eb'
down_revision = '90b2b05c29de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('syslog')
    op.drop_index('email', table_name='users')
    op.drop_table('users')
    op.drop_index('orderNum', table_name='orders')
    op.drop_table('orders')
    op.drop_table('role_permission')
    op.drop_table('permission')
    op.drop_table('users_role')
    op.drop_table('role')
    op.drop_table('traveller')
    op.drop_table('order_traveller')
    op.drop_table('member')
    op.drop_table('product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', mysql.VARCHAR(length=32), server_default=sa.text("''"), nullable=False),
    sa.Column('productNum', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('productName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('cityName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('DepartureTime', mysql.TIMESTAMP(), nullable=True),
    sa.Column('productPrice', mysql.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('productDesc', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('productStatus', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('member',
    sa.Column('id', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('NAME', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('nickname', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('phoneNum', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('order_traveller',
    sa.Column('orderId', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('travellerId', mysql.VARCHAR(length=32), nullable=False),
    sa.ForeignKeyConstraint(['orderId'], ['orders.id'], name='order_traveller_ibfk_1'),
    sa.ForeignKeyConstraint(['travellerId'], ['traveller.id'], name='order_traveller_ibfk_2'),
    sa.PrimaryKeyConstraint('orderId', 'travellerId'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('traveller',
    sa.Column('id', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('NAME', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('sex', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('phoneNum', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('credentialsType', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('credentialsNum', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('travellerType', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('role',
    sa.Column('id', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('roleName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('roleDesc', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('users_role',
    sa.Column('userId', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('roleId', mysql.VARCHAR(length=32), nullable=False),
    sa.ForeignKeyConstraint(['roleId'], ['role.id'], name='users_role_ibfk_2'),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], name='users_role_ibfk_1'),
    sa.PrimaryKeyConstraint('userId', 'roleId'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('permission',
    sa.Column('id', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('permissionName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('url', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('role_permission',
    sa.Column('permissionId', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('roleId', mysql.VARCHAR(length=32), nullable=False),
    sa.ForeignKeyConstraint(['permissionId'], ['permission.id'], name='role_permission_ibfk_1'),
    sa.ForeignKeyConstraint(['roleId'], ['role.id'], name='role_permission_ibfk_2'),
    sa.PrimaryKeyConstraint('permissionId', 'roleId'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('orders',
    sa.Column('id', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('orderNum', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('orderTime', mysql.TIMESTAMP(), nullable=True),
    sa.Column('peopleCount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('orderDesc', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('payType', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('orderStatus', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('productId', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('memberId', mysql.VARCHAR(length=32), nullable=True),
    sa.ForeignKeyConstraint(['memberId'], ['member.id'], name='orders_ibfk_2'),
    sa.ForeignKeyConstraint(['productId'], ['product.id'], name='orders_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('orderNum', 'orders', ['orderNum'], unique=True)
    op.create_table('users',
    sa.Column('id', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('PASSWORD', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('phoneNum', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('STATUS', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('email', 'users', ['email'], unique=True)
    op.create_table('syslog',
    sa.Column('id', mysql.INTEGER(display_width=32), autoincrement=True, nullable=False),
    sa.Column('visitTime', mysql.TIMESTAMP(), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('ip', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('url', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('executionTime', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('method', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('post')
    # ### end Alembic commands ###
