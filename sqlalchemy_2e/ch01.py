"""
janus.base
~~~~~~~~~~~~~~~~~~~~~~~

功能:

版权所有 © 2020
"""
from sqlalchemy import create_engine
from sqlalchemy import MetaData  # 元数据
from sqlalchemy_2e.config_local import TARGET_DB_CONFIG

# 创建引擎
engine = create_engine(
    '{engine}+{driver}://{user}:{password}@{host}:{port}/{dbname}?charset={charset}'.format(**TARGET_DB_CONFIG),
    pool_size=TARGET_DB_CONFIG['pool_size'],
    max_overflow=TARGET_DB_CONFIG['max_overflow'],
    pool_recycle=TARGET_DB_CONFIG['pool_recycle']
)

# 创建连接
connection = engine.connect()

# 初始化元数据
metadata = MetaData()

from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime

"""
default=datetime.now(): 默认设置为首次初始化得时间
default=datetime.now  : 可以得到实例化和每个更新的时间
创建列一般思路：类型, 长度,　精度, 主键, 索引,　重复, 默认值

unique=True：　唯一字段
index=True: 设置索引
primary_key=True：　设置主键
nullable=False：　字段不为空
"""
# 创建列
cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2))
                )

users = Table('users', metadata,
              Column('user_id', Integer(), primary_key=True),
              Column('username', String(15), nullable=False, unique=True),
              Column('email_address', String(255), nullable=False),
              Column('phone', String(20), nullable=False),
              Column('password', String(25), nullable=False),
              Column('created_on', DateTime(), default=datetime.now),
              Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
              )

orders = Table('orders', metadata,
               Column('order_id', Integer(), primary_key=True),
               Column('user_id', ForeignKey('users.user_id')),
               )

line_items = Table('line_items', metadata,
                   Column('line_items_id', Integer(), primary_key=True),
                   Column('order_id', ForeignKey('orders.order_id')),
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),
                   Column('quantity', Integer()),
                   Column('extended_cost', Numeric(12, 2))
                   )

# 模型持久化到数据库
metadata.create_all(engine)

# 键和约束
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint, ForeignKeyConstraint

# 复合键（多个主键）
PrimaryKeyConstraint('user_id', name='user_py')

# 唯一约束, 确保没有重复的值
UniqueConstraint('username', name='uix_sername')

# 检查约束,　用于确保列数据和一组由用户定义的标准匹配
# 确保unit_cost永远不会小于0.00
CheckConstraint('unit_cost >= 0', name='unit_cost_postive')

# 外键约束: 关联表作用
ForeignKeyConstraint(['order_id'], ['orders.order_id'])