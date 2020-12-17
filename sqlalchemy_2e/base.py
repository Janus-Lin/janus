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

metadata.create_all(engine)
