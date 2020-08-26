"""
janus.python_base3.04_dict
~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 字典

版权所有 © 2020
"""

"""
字典： 通过名称来访问其各个值的数据结构。这种数据结构称为映射（mapping）。
字典是Python中唯的内置映射类型，其中的值不按顺序排列，而是存储在键下。键可能是数、字符串或元组。
dict其实根本就不是函数，而是一个类, 映射可以解决很多性能问题，不必像list一样循环处理。
"""
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
d = dict(name='Gumby', age=42)

# 字典的基本行为在很多方面都类似于序列。
len(d)  # 返回字典d包含的项（键值对） d[k]返回与键k相关联的值。
d['k'] = 'v'  # 将值v关联到键k。
del d['k']  # 删除键为k的项。
print('k' in d)  # 检查字典d是否包含键为k的项。

# 注意：
"""
键的类型：字典中的键可以是整数，但并非必须是整数
自动添加：即便是字典中原本没有的键，也可以给它赋值，这将在字典中创建一个然而，如果不使用append或其他类似的方法，就不能给列表中没有的元素赋值。
成员资格：表达式k in d（其中d是一个字典）查找的是键而不是值，而表达式v in l（其中l是一个列表）查找的是值而不是索引。检查字典是否包含指定的键的效率更高
"""

# 字典方法
# clear: 删除所有的字典项，这种操作是就地执行的（就像list.sort一样），因此什么都不返回（或者说返回None）
d.clear()

# copy: 返回一个新字典，其包含的键值对与原来的字典相同（这个方法执行的是浅复制，因为值本身是原件，而非副本）
# 当替换副本中的值时，原件不受影响。然而，如果修改副本中的值（就地修改而不是替换），原件也将发生变化，因为原件指向的也是被修改的值
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(x, y)

# 为避免这种问题，一种办法是执行深复制，即同时复制值及其包含的所有值，等等。为此，可使用模块copy中的函数deepcopy
from copy import deepcopy

d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(x, y)

# fromkeys: 创建一个新字典，其中包含指定的键，且每个键对应的值都是None。
a = {}.fromkeys(['name', 'age'])
print(a)
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age'], '(unknown)'))  # 不想使用默认值None，可提供特定的值

# get： 为访问字典项提供了宽松的环境。通常，如果你试图访 d.get('name', 'N/A')问字典中没有的项，将引发错误
print(d.get('name'))  # d['name']会报错
print(d.get('name', 'N/A'))  # key不存在返回特定值

# items： 返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式。字典项在列表中的排列顺序不确定
# 返回值属于一种名为字典视图的特殊类型。字典视图可用于迭代
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())

# keys: 返回一个字典视图，其中包含指定字典中的键。
print(d.keys())

# pop: 可用于获取与指定键相关联的值，并将该键值对从字典中删除
d.pop('title')
print(d)

# popitem: 类似于list.pop，但list.pop弹出列表中的最后一个元素，而popitem随机地弹出一个字典项，因为字典项的顺序是不确定的，没有“最后一个元素”的概念
d.popitem()
print(d)

# 指定的键不存在时，setdefault返回指定的值并相应地更新字典。如果指定的键存在，就返回其值，并保持字典不变。与get一样，值是可选的；如果没有指定，默认为None。
d = {}
d.setdefault('name', 'N/A')
print(d)

# update: 使用一个字典中的项来更新另一个字典
y = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
x = {'title': 'Python Language Website'}
y.update(x)
print(y)

# values: 返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的图可能包含重复的值
d = {1: 1, 2: 2, 3: 3, 4: 1}
print(d.values())
"""
本章介绍的新函数
函 数                                描 述
dict(seq)                           从键值对、映射或关键字参数创建字典
"""