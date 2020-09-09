"""
janus.python_base3.13_db_api
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 数据库api

版权所有 © 2020
"""
# DB API定义了一些构造函数和常量（单例），用于提供特殊的类型和值.
import sqlite3

"""
Python DB API： 这个API定义了一个简单的标准化接口，所有数据库包装器模块都必须遵循它，这让编写使用多个不同数据库的程序更容易。
连接： 连接对象表示到SQL数据库的通信链路，使用方法cursor可从连接获得游标。你还可使用连接对象来提交或回滚事务。使用完数据库后，就可将连接关闭了。
游标： 游标用于执行查询和查看结果。可逐行取回查询结果，也可一次取回很多（或全部）行。
类型和特殊值： DB API指定了一组构造函数和特殊值的名称。构造函数用于处理日期和时间对象，还有二进制数据对象；而特殊值用于表示关系型数据库的类型，如STRING、NUMBER和DATETIME。
SQLite： 这是一个小型的嵌入式SQL数据库，标准Python发行版中包含其Python包装器，即模块sqlite3。这个数据库速度快、易于使用，且不要求搭建专门的服务器。
"""

api_attribute = {
    'apilevel': '使用的Python DB API版本',
    'threadsafety': '模块的线程安全程度如何',
    'paramstyle': '在SQL查询中使用哪种参数风格'
}

# Python DB API指定的异常
"""
异 常              超 类                  描 述
StandardError                           所有异常的超类
Warning           StandardError         发生非致命问题时引发
Error             StandardError         所有错误条件的超类
InterfaceError    Error                 与接口（而不是数据库）相关的错误
DatabaseError     Error                 与数据库相关的错误的超类
DataError         DatabaseError         与数据相关的问题，如值不在合法的范围内
OperationalError  DatabaseError         数据库操作内部的错误
IntegrityError    DatabaseError         关系完整性遭到破坏，如键未通过检查
InternalError     DatabaseError         数据库内部的错误，如游标无效
ProgrammingError  DatabaseError         用户编程错误，如未找到数据库表
NotSupportedError DatabaseError         请求不支持的功能，如回滚
"""
# 连接和游标: 函数connect的常用参数
"""
参 数 名   描 述                       是否可选
dsn       数据源名称，具体含义随数据库而异  否
user      用户名                      是
password  用户密码                     是
host      主机名                      是
database  数据库名称                   是
"""
# 连接对象的方法
# 方法rollback可能不可用，因为并非所有的数据库都支持事务（事务其实就是一系列操作）。可用时，这个方法撤销所有未提交的事务
"""
方 法 名    描 述
close()    关闭连接对象。之后，连接对象及其游标将不可用
commit()   提交未提交的事务——如果支持的话；否则什么都不做
rollback() 回滚未提交的事务（可能不可用）
cursor()   返回连接的游标对象
"""
# 游标对象的方法
"""
名 称                         描 述
callproc(name[, params])     使用指定的参数调用指定的数据库过程（可选）
close()                      关闭游标。关闭后游标不可用
execute(oper[, params])      执行一个SQL操作——可能指定参数
executemany(oper, pseq)      执行指定的SQL操作多次，每次都序列中的一组参数
fetchone()                   以序列的方式取回查询结果中的下一行；如果没有更多的行，就返回None
fetchmany([size])            取回查询结果中的多行，其中参数size的值默认为arraysize
fetchall()                   以序列的序列的方式取回余下的所有行
nextset()                    跳到下一个结果集，这个方法是可选的
setinputsizes(sizes)         用于为参数预定义内存区域
setoutputsize(size[, col])   为取回大量数据而设置缓冲区长度
"""
# 游标对象的属性
"""
名 称                 描 述
description          由结果列描述组成的序列（只读）
rowcount             结果包含的行数（只读）
arraysize fetchmany  返回的行数，默认为1
"""
# 类型: 对于插入到某些类型的列中的值，底层SQL数据库可能要求它们满足一定的条件。为了能够与底层SQL数据库正确地互操作，

conn = sqlite3.connect('somedatabase.db')  # 获取连接
curs = conn.cursor()  # 接获得游标
conn.commit()  # 提交所做的修改
conn.close()  # 关闭连接

# ? 需要补充mysql数据库操作实例
