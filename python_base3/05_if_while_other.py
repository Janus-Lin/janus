"""
janus.python_base3.05_if_while_other
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 判断， 循环

版权所有 © 2020
"""

# 别名： 提高代码可维护性（log函数使用）
from datetime import date as date01

# 并行赋值（序列解包）： 将一个序列（或任何可迭代对象）解包，并将得到的值存储到一系列变量中。下面用例子进行解释。
values = 1, 2, 3
x, y, z = values
print(x, y, z)
x, y = y, x
print(x, y)

# 可使用星号运算符（*）来收集多余的值,还可将带星号的变量放在其他位置。带星号的变量最终包含的总是一个列表
a, b, *rest = [1, 2, 3, 4]
print(rest)

# 链式赋值：是一种快捷方式，用于将多个变量关联到同一个值。这有点像前一节介绍的并行赋值，但只涉及一个值
x = y = 6
print(x, y)

# 增强赋值: 可以不编写代码x = x + 1，而将右边表达式中的运算符（这里是+）移到赋值运算符（=）的前面，从而写成x += 1。
# 只要使用的双目运算符可用于这些数据类型
x = 1
x += 1
x *= 2
print(x)
fnord = '1212'
fnord += 'bdbasd'
fnord *= 2
print(fnord)

# 代码块：缩进的乐趣, 代码块是一组语句，可在满足条件时执行（if语句），可执行多次（循环），等等。代码块是通过缩进代码（即在前面加空格）来创建的。
# 用作布尔表达式（如用作if语句中的条件）时，下面的值都将被解释器视为假：False None 0 "" () [] {}
print(True == 1)

"""
表 达 式   描 述
x == y    x 等于y
x < y     x小于y
x > y     x大于y
x >= y    x大于或等于y
x <= y    x小于或等于y
x != y    x不等于y
x is y    x和y是同一个对象
x is not y  x和y是不同的对象
x in y      x是容器（如序列）y的成员
x not in y  x不是容器（如序列）y的成员
"""
# 布尔运算: 短路逻辑(or, and将“绕过”第二个值。用于提高运行效率)
# 断言: 如果知道必须满足特定条件，程序才能正确地运行，可在程序中添加assert语句充当检查点，这很有帮助
age = 10
assert 0 < age < 100
# assert  age > 100, 'The age must be realistic'

# while 循环: 给定结束条件，条件为真时反复执行代码块。
# for 循环： 可迭代对象是可使用for循环进行遍历的对象。for循环的优点之一是，可在其中使用序列解包。
for number in range(1, 10):
    print(number)

# 迭代字典：无序的
"""
迭代字典的键或值时，一定会处理所有的
键或值，但不知道处理的顺序。如果顺序很重要，可将键或值存储在一个列表中并对列
表排序，再进行迭代。要让映射记住其项的插入顺序，可使用模块collections中的
OrderedDict类。
"""
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])

for key, value in d.items():
    print(key, 'corresponds to', value)

# 迭代方式
# 01-并行迭代：想同时迭代多个序列
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')

# 升级方法： zip缝合（任意数量的序列）并返回一个由元组组成的序列。当序列的长度不同时，函数zip将在最短的序列用完后停止“缝合”。
list(zip(names, ages))
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')

# 02-迭代时获取索引
strings = [1, 2, 3, 4, 5, 6, 7]
for index, string in enumerate(strings):
    if 7 == string:
        strings[index] = 7777
print(strings)

# 03-反向迭代(reversed)和排序(sorted)后再迭代
# 要按字母表排序，可先转换为小写。为此，可将sort或sorted的key参数设置为str.lower。
# 例如，sorted("aBc", key=str.lower)返回['a', 'B', 'c']。
print(sorted([4, 3, 6, 8, 3]))
print(sorted('Hello, world!'))
print(list(reversed('Hello, world!')))
print(''.join(reversed('Hello, world!')))

# 04-跳出循环:
# break
from math import sqrt

for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

#  continue
for x in [1, 2, 3, 4, 5]:
    if x == 1: continue
    if x == 2: continue
    if x == 3: continue
    print(x)

# while True/break成例
# while True:
#     word = input('Please enter a word: ')
#     if not word: break
#     # 使用这个单词做些事情：
#     print('The word was ', word)


# 列表推导:
# 简单推导
lis = [x * x for x in range(10)]
print(lis)

# 带判断推导
lis_if = [x * x for x in range(10) if x % 3 == 0]
print(lis_if)

# 双重推导
lis_more = [(x, y) for x in range(3) for y in range(3)]
print(lis_more)

# 上式等价于
result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))

# 双重推导 + 判断
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
lis_more_if = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
print(lis_more_if)

# 字典推导
squares = {i: i ** 2 for i in range(10)}
print(squares)

# 三人行
# pass: 什么都不用做，占位符
if ' ' == '212':
    pass
else:
    print()

# del： 不仅会删除到对象的引用，还会删除名称本身.
# 事实上，在Python中，根本就没有办法删除值，而且你也不需要这样做，因为对于你不再使用的值，Python解释器会立即将其删除
x = [1, 2, 3, 4, 5]
del x[0]
print(x)

"""
命名空间（作用域）是个重要的概念，将在下一章深入讨论，但就目前而言，你可将命
名空间视为放置变量的地方，类似于一个看不见的字典。因此，当你执行赋值语句x = 1
时，将在当前命名空间存储键x和值1。当前命名空间通常是全局命名空间（到目前为止，
我们使用的大都是全局命名空间），但并非必然如此。
"""
# exec: 将字符串作为代码执行(scope: 解决命名空间问题)
from math import sqrt
scope = {}
exec('sqrt = 1', scope)
sqrt(4)
scope['sqrt']


# eval是一个类似于exec的内置函数。exec执行一系列Python语句，而eval计算用字符串表示的Python表达式的值，并返回结果
# （exec什么都不返回，因为它本身是条语句）
print(eval('1 * 2'))

# 向exec或eval提供命名空间时，可在使用这个命名空间前在其中添加一些值。
scope = {}
scope['x'] = 2
scope['y'] = 3
print(eval('x * y', scope))

# 同样，同一个命名空间可用于多次调用exec或eval。
scope = {}
scope['x'] = 2
scope['y'] = 3
eval('x * y', scope)

"""
本章介绍的新函数
函 数                                描 述
chr(n)                              返回一个字符串，其中只包含一个字符，这个字符对应于传入的顺序值n（0 ≤n < 256）
eval(source[,globals[,locals]])     计算并返回字符串表示的表达式的结果
exec(source[, globals[, locals]])   将字符串作为语句执行
enumerate(seq)                      生成可迭代的索引值对
ord(c)                              接受一个只包含一个字符的字符串，并返回这个字符的顺序值（一个整数）
range([start,] stop[, step])        创建一个由整数组成的列表
reversed(seq)                       按相反的顺序返回seq中的值，以便用于迭代
sorted(seq[,cmp][,key][,reverse])   返回一个列表，其中包含seq中的所有值且这些值是经过排序的
xrange([start,] stop[, step])       创建一个用于迭代的xrange对象
zip(seq1, seq2,...)                 创建一个适合用于并行迭代的新序列
"""