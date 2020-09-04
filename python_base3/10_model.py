"""
janus.python_base3.10_medel
~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 模块, 标准库

版权所有 © 2020
"""

"""
模块： 模块基本上是一个子程序，主要作用是定义函数、类和变量等。模块包含测试代码时，
应将这些代码放在一条检查name == '__main__'的if语句中。如果模块位于环境变量PYTHONPATH包含的目录中，
就可直接导入它；要导入存储在文件foo.py中的模块，可使用语句import foo。要让代码是可重用的，务必将其模块化.
  
包： 包不过是包含其他模块的模块。包是使用包含文件__init__.py的目录实现的。

探索模块： 在交互式解释器中导入模块后，就可以众多不同的方式对其进行探索，其中包括使用dir、查看变量__all__以及使用函数help。
文档和源代码也是获取信息和洞见的极佳来源。

标准库： Python自带多个模块，统称为标准库。本章介绍了其中的几个。
    sys： 这个模块让你能够访问多个与Python解释器关系紧密的变量和函数。
    os： 这个模块让你能够访问多个与操作系统关系紧密的变量和函数。
    fileinput： 这个模块让你能够轻松地迭代多个文件或流的内容行。
    sets、heapq和deque： 这三个模块提供了三种很有用的数据结构。内置类型set也实现了集合。
    time： 这个模块让你能够获取当前时间、操作时间和日期以及设置它们的格式。
    random： 这个模块包含用于生成随机数，从序列中随机地选择元素，以及打乱列表中元素的函数。
    shelve： 这个模块用于创建永久性映射，其内容存储在使用给定文件名的数据库中。
    re： 支持正则表达式的模块。
"""

"""
函 数                 描 述
dir(obj)             返回一个按字母顺序排列的属性名列表
help([obj])          提供交互式帮助或有关特定对象的帮助信息
imp.reload(module)   返回已导入的模块的重载版本
"""

# 模块
import math

print(math.sin(0))

# 设置模块路径
import sys

sys.path.append('/home/lin/PycharmProjects/engineer/janus/python_base3/tools.py')
import tools

tools.qq()

# 第二次导入模块时什么都不会发生，避免重复导入
# 要重新加载模块，可使用模块importlib中的函数reload，它接受一个参数（要重新加载的模块），并返回重新加载的模块.
import importlib

hello = importlib.reload(tools)

import sys, pprint

# 要打印的数据结构太大，一行容纳不下，可使用模块pprint中的函数pprint（
pprint.pprint(sys.path)
# 只要模块位于类似于site-packages这样的地方，所有的程序就都能够导入它，标准导入库的位置。

# 环境变量（添加python解释器）： export PYTHONPATH=$PYTHONPATH:~/python
"""
一种简单的包布局
文件/目录                       描 述
~/python/                      PYTHONPATH中的目录
~/python/drawing/              包目录（包drawing）
~/python/drawing/__init__.py   包代码（模块drawing）
~/python/drawing/colors.py     模块colors
~/python/drawing/shapes.py     模块shapes
"""
"""
完成这些准备工作后，下面的语句都是合法的：
import drawing # (1) 导入drawing包
import drawing.colors # (2) 导入drawing包中的模块colors 
from drawing import shapes # (3) 导入模块shapes
"""

# 模块包含什么
# 函数dir: 列出对象的所有属性（对于模块，它列出所有的函数、类、变量等）。
import copy

print(dir(copy))
print([n for n in dir(copy) if not n.startswith('_')])

# 果不设置__all__，则会在以import *方式导入时，导入所有不以下划线打头的全局名称.
"""
从copy.py复制而来的
__all__ = ["Error", "copy", "deepcopy"]
from copy import *
"""
print(copy.__all__)

# help: 一个标准函数可提供你通常需要的所有信息.
help(copy.copy)
print(copy.copy.__doc__)

# 文档是有关模块信息的自然来源
print(range.__doc__)

# 探索源码
print(copy.__file__)

# sys
"""
函数/变量                     描 述
argv                        命令行参数，包括脚本名
exit([arg])                 退出当前程序，可通过可选参数指定返回值或错误消息
modules                     一个字典，将模块名映射到加载的模块
path                        一个列表，包含要在其中查找模块的目录的名称
platform                    一个平台标识符，如sunos5或win32
stdin                       标准输入流——一个类似于文件的对象
stdout                      标准输出流——一个类似于文件的对象
stderr                      标准错误流——一个类似于文件的对象
"""

# os
"""
函数/变量         描 述
environ         包含环境变量的映射
system(command) 在子shell中执行操作系统命令
sep             路径中使用的分隔符
pathsep         分隔不同路径的分隔符
linesep         行分隔符（'\n'、'\r'或'\r\n'）
urandom(n)      返回n个字节的强加密随机数据
"""
# 这将弹出指定的网页
import webbrowser

# webbrowser.open('http://www.python.org')

# fileinput
"""
函 数                                 描 述
input([files[, inplace[, backup]]])  帮助迭代多个输入流中的行
filename()                           返回当前文件的名称
lineno()                             返回（累计的）当前行号
filelineno()                         返回在当前文件中的行号
isfirstline()                        检查当前行是否是文件中的第一行
isstdin()                            检查最后一行是否来自sys.stdin
nextfile()                           关闭当前文件并移到下一个文件
close()                              关闭序列
"""
# import fileinput
#
# for line in fileinput.input(inplace=True):
#     line = line.rstrip()
#     num = fileinput.lineno()
#     print('{:<50} # {:2d}'.format(line, num))


# 集合: 用于各种数据集合运算
print(set(range(10)))

a = {1, 2, 3}
b = {2, 3, 4}
c = a & b
print(a.union(b))
print(a | b)
print(c.issubset(a))
print(c <= a)
print(c.issuperset(a))
print(c >= a)
print(a.intersection(b))
print(a & b)
print(a.difference(b))
print(a - b)
print(a.symmetric_difference(b))
print(a ^ b)
print(a.copy())

# 集合只能包含不可变（可散列）的值
a = set([1, 2])
b = set([3, 4])
# a.add(b) 报错
a.add(frozenset(b))
print(a)

# ?堆: 一种优先队列优先队列让你能够以任意顺序添加对象，并随时（可能是在两次添加对象之间）找出（并删除）最小的元素。
# 相比于列表方法min，这样做的效率要高得多,，不能将它用于普通列表，而只能用于使用各种堆函数创建的列表
"""
函 数                 描 述
heappush(heap, x)    将x压入堆中
heappop(heap)        从堆中弹出最小的元素
heapify(heap)        让列表具备堆特征
heapreplace(heap, x) 弹出最小的元素，并将x压入堆中
nlargest(n, iter)    返回iter中n个最大的元素
nsmallest(n, iter)   返回iter中n个最小的元素
"""
from heapq import *
from random import shuffle

data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)

print(heap)
heappush(heap, 0.5)
print(heap)

# ?双端队列（及其他集合）:在需要按添加元素的顺序进行删除时，双端队列很有用。在模块collections中，包含类型deque以及其他几个集合（collection）类型
"""
双端队列很有用，因为它支持在队首（左端）高效地附加和弹出元素，而使用列表无法这样做。
另外，还可高效地旋转元素（将元素向右或向左移，并在到达一端时环绕到另一端）。双端队列对
象还包含方法extend和extendleft，其中extend类似于相应的列表方法，而extendleft类似于
appendleft。请注意，用于extendleft的可迭代对象中的元素将按相反的顺序出现在双端队列中。
"""
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
q.pop()
q.popleft()
q.rotate(3)
q.rotate(-1)

#  time:模块time包含用于获取当前时间、操作时间和日期、从字符串中读取日期、将日期格式化为字符串的函数。
"""
函 数                       描 述
asctime([tuple])           将时间元组转换为字符串
localtime([secs])          将秒数转换为表示当地时间的日期元组
mktime(tuple)              将时间元组转换为当地时间
sleep(secs)                休眠（什么都不做）secs秒
strptime(string[, format]) 将字符串转换为时间元组
time()                     当前时间（从新纪元开始后的秒数以UTC为准）
"""
import time
print( time.asctime())

# datetime
# timeit

# random: 包含生成伪随机数的函数，有助于编写模拟程序或生成随机输出的程序。
# 如果你要求真正的随机（如用于加密或实现与安全相关的功能），应考虑使用模块os中的函数urandom
"""
函 数               描 述
random()           返回一个0~1（含）的随机实数
getrandbits(n)     以长整数方式返回n个随机的二进制位
uniform(a, b)      返回一个a~b（含）的随机实数
randrange([start], stop, [step]) 从range(start, stop, step)中随机地选择一个数
choice(seq)        从序列seq中随机地选择一个元素
shuffle(seq[, random]) 就地打乱序列seq
sample(seq, n)     从序列seq中随机地选择n个值不同的元素
"""
from random import *
from time import *
date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
random_time = uniform(time1, time2)
print(asctime(localtime(random_time)))

# 潜在的陷阱: shelve.open后的赋值
# 正则表达式： re
# 模板：是一种文件，可在其中插入具体的值来得到最终的文本。
"""
argparse：在UNIX中，运行命令行程序时常常需要指定各种选项（开关），Python解释器就是这样的典范。

cmd：这个模块让你能够编写类似于Python交互式解释器的命令行解释器。你可定义命令，让用户能够在提示符下执行它们。

csv： 能够轻松地读写CSV文件, 处理CSV格式的一些棘手部分.

datetime： 如果模块time不能满足你的时间跟踪需求，模块datetime很可能能够满足。

difflib：这个库让你能够确定两个序列的相似程度，还让你能够从很多序列中找出与指定序列最为相似的序列。

enum： 枚举类型是一种只有少数几个可能取值的类型。

functools： 这个模块提供的功能是，让你能够在调用函数时只提供部分参数（部分求值，partial evaluation），以后再填充其他的参数.

hashlib：使用这个模块可计算字符串的小型“签名”（数）。计算两个不同字符串的签名时，几乎可以肯定得到的两个签名是不同的。

itertools：包含大量用于创建和合并迭代器（或其他可迭代对象）的工具，其中包括可以串接可迭代对象、创建返回无限连续整数的迭代器（类似于range，但没有上限）、反复
遍历可迭代对象以及具有其他作用的函数。

logging：使用print语句来确定程序中发生的情况很有用。要避免跟踪时出现大量调试输出，可将这些信息写入日志文件中。

statistics：计算一组数的平均值并不那么难，但是要正确地获得中位数，以确定总体标准偏差和样本标准偏差之间的差别.

timeit、profile和trace：模块timeit（和配套的命令行脚本）是一个测量代码段执行时间的工具。这个模块暗藏玄机，度量性能时你可能应该使用它而不是模块time。
模块profile（和配套模块pstats）可用于对代码段的效率进行更全面的分析。模块trace可帮助你进行覆盖率分析（即代码的哪些部分执行了，哪些部分没有执行），
这在编写测试代码时很有用。

"""
