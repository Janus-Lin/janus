"""
fdp.config_local
~~~~~~~~~~~~~~~~

功能:

版权所有 © 2019, 美通智投（北京）有限公司
"""
import os

# 目标数据库的配置(自己本地)
TARGET_DB_CONFIG = {
    'engine': os.getenv('TARGET_DB_ENGINE', 'mysql'),
    'driver': os.getenv('TARGET_DB_DRIVER', 'pymysql'),
    'user': os.getenv('TARGET_DB_USER', 'root'),
    'password': os.getenv('TARGET_DB_PASSWORD', 'lin123456'),
    'host': os.getenv('TARGET_DB_HOST', '127.0.0.1'),
    'port': os.getenv('TARGET_DB_PORT', '3306'),
    'dbname': os.getenv('TARGET_DB_NAME', 'sqlalchemy'),
    'charset': os.getenv('TARGET_DB_CHARSET', 'utf8'),
    'pool_size': 25,
    'max_overflow': 25,
    'pool_recycle': 3600,  # 回收链接时间
    'check_name': '本地'
}

# sqlalchemy db URI
SQLALCHEMY_DATABASE_URI = '{engine}+{driver}://{user}:{password}@{host}:{port}/{dbname}?charset={charset}'.format(
    **TARGET_DB_CONFIG)
