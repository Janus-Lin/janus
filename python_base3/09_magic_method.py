"""
janus.python_base3.09_magic_method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 魔法方法, 特性, 迭代器

版权所有 © 2020
"""


# 构造函数:  __init__, 初始化方法

class FooBar:
    def __init__(self, somevar2):
        self.somevar = 42
        self.somevar2 = somevar2


f = FooBar(somevar2='hello!')
print(f.somevar)
print(f.somevar2)


# 析构函数: 在对象被销毁（作为垃圾被收集）前被调用，但鉴于你无法知道准确的调用时间，建议尽可能不要使用__del__.

# super: 调用父类构造方法, 将在所有的超类（以及超类的超类，等等）中查找，直到找到指定的属性或引发AttributeError异常.
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()  # 不调用super, 子类重写构造方法会覆盖父类构造方法.
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


# 基本的序列和映射协议?
"""
__len__(self)：这个方法应返回集合包含的项数，对序列来说为元素个数，对映射来说为键值对数。
如果__len__返回零（且没有实现覆盖这种行为的__nonzero__），对象在布尔上下文中将被视为假（就像空的列表、元组、字符串和字典一样）。
"""

"""
__getitem__(self, key)：这个方法应返回与指定键相关联的值。对序列来说，键应该是0~n 1的整数（也可以是负数，这将在后面说明），
其中n为序列的长度。对映射来说，键可以是任何类型.
"""

"""
__setitem__(self, key, value)：这个方法应以与键相关联的方式存储值，以便以后能够使用__getitem__来获取。
当然，仅当对象可变时才需要实现这个方法.
"""

"""
__delitem__(self, key)：这个方法在对对象的组成部分使用__del__语句时被调用，应删除与key相关联的值。
同样，仅当对象可变（且允许其项被删除）时，才需要实现这个方法.
"""


# 从 list、dict 和 str 派生:
# 带访问计数器的列表
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

cl = CounterList(range(10))
print(cl)
cl.reverse()
del cl[3:6]
print(cl.counter)
cl[4] + cl[2]
print(cl.counter)