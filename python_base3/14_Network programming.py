"""
janus.python_base3.Network programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 网络编程

版权所有 © 2020
"""
# 模块 urllib 和 urllib2
from urllib.request import urlopen, urlretrieve

"""
套接字和模块socket： 套接字是让程序（进程）能够通信的信息通道，这种通信可能需要通过网络进行。
模块socket让你能够在较低的层面访问客户端套接字和服务器套接字。服务器套接字在指定的地址处监听客户端连接，而客户端套接字直接连接到服务器。

rllib和urllib2： 这些模块让你能够从各种服务器读取和下载数据，为此你只需提供指向数据源的URL即可。模块urllib是一种比较简单的实现，
而urllib2功能强大、可扩展性极强。这两个模块都通过诸如urlopen等函数来完成工作。

框架SocketServer： 这个框架位于标准库中，包含一系列同步服务器基类，让你能够轻松地编写服务器。它还支持使用CGI的简单Web（HTTP）服务器。
如果要同时处理多个连接，必须使用支持分叉或线程化的混合类。

elect和poll： 这两个函数让你能够在一组连接中找出为读取和写入准备就绪的连接。这意味着你能够以循环的方式依次为多个连接提供服务，
从而营造出同时处理多个连接的假象。另外，相比于线程化或分叉，虽然使用这两个函数编写的代码要复杂些，但解决方案的可伸缩性和效率要高得多。

Twisted：这是Twisted Matrix Laboratories开发的一个框架，功能丰富而复杂，支持大多数主要的网络协议。
虽然这个框架很大且其中使用的一些成例看起来宛如天书，但其基本用法简单而直观。框架Twisted也是异步的，因此效率和可伸缩性都非常高。
对很多自定义网络应用程序来说，使用Twisted来开发很可能是最佳的选择。
"""

"""
函 数                                          描 述
urllib.urlopen(url[, data[, proxies]])        根据指定的URL打开一个类似于文件的对象
urllib.urlretrieve(url[,fname[,hook[,data]]]) 下载URL指定的文件
urllib.quote(string[, safe])                  替换特殊的URL字符
urllib.quote_plus(string[, safe])             与quote一样，但也将空格替换为+
urllib.unquote(string)                        与quote相反
urllib.unquote_plus(string)                   与quote_plus相反
urllib.urlencode(query[, doseq])              对映射进行编码，以便用于CGI查询中
select.select(iseq, oseq, eseq[, timeout])    找出为读/写做好了准备的套接字
select.poll()                                 创建一个轮询对象，用于轮询套接字
reactor.listenTCP(port, factory)              监听连接的Twisted函数
reactor.run()                                 启动主服务器循环的Twisted函数
"""
# 最简单的服务器
# import socket

# s = socket.socket()
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
# s.listen(5)
# while True:
#     c, addr = s.accept()
#     print('Got connection from', addr)
#     c.send('Thank you for connecting')
#     c.close()
#
# # 最简单的客户端
# import socket
#
# s = socket.socket()
# host = socket.gethostname()
# port = 1234
# s.connect((host, port))
# print(s.recv(1024))


# 打开远程文件
webpage = urlopen('http://www.baidu.com')

# 获取远程文件
urlretrieve('http://www.baidu.com', 'data/baidu.html')
# 标准库中一些与网络相关的模块
"""
模 块                    描 述
asynchat                包含补充asyncore的功能（参见第24章asyncore 异步套接字处理程序（参见第24章）
cgi                     基本的CGI支持（参见第15章）
Cookie Cookie           对象操作，主要用于服务器
cookielib               客户端Cookie支持
email                   电子邮件（包括MIME）支持
ftplib FTP              客户端模块
gopherlib Gopher        客户端模块
httplib HTTP            客户端模块
imaplib IMAP4           客户端模块
mailbox                 读取多种邮箱格式
mailcap                 通过mailcap文件访问MIME配置
mhlib                   访问MH邮箱
nntplib NNTP            客户端模块（参见第23章）
poplib POP              客户端模块
robotparser             解析Web服务器robot文件
SimpleXMLRPCServer      一个简单的XML-RPC服务器（参见第27smtpd SMTP服务器模块
smtplib                 SMTP客户端模块
telnetlib               Telnet 客户端模块
urlparse                用于解读URL 
xmlrpclib XML-RPC       客户端支持（参见第27章）
"""

# 基于SocketServer的极简服务器
#  Twisted
