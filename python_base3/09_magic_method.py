"""
janus.python_base3.09_magic_method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 魔法方法, 特性, 迭代器, 生成器

版权所有 © 2020
"""
"""
新式类和旧式类：Python类的工作方式在不断变化。较新的Python 2版本有两种类，其中旧式类正在快速退出舞台。
新式类是Python 2.2引入的，提供了一些额外的功能，如支持函数super和property，而旧式类不支持
要创建新式类，必须直接或间接地继承object或设置__metaclass__.

魔法方法：Python中有很多特殊方法，其名称以两个下划线开头和结尾。这些方法的功能各不相同，
但大都由Python在特定情况下自动调用。例如__init__是在对象创建后调用的。

构造函数：很多面向对象语言中都有构造函数，对于你自己编写的每个类，都可能需要为它实现一个构造函数。
构造函数名为__init__，在对象创建后被自动调用.

重写：类可重写其超类中定义的方法（以及其他任何属性），为此只需实现这些方法即可。要调用被重写的版本，
可直接通过超类调用未关联版本（旧式类），也可使用函数super来调用（新式类）。

序列和映射：要创建自定义的序列或映射，必须实现序列和映射协议指定的所有方法，其中包括__getitem__和__setitem__等魔法方法。
通过从list（或UserList）和dict（或UserDict）派生，可减少很多工作量。

迭代器：简单地说，迭代器是包含方法__next__的对象，可用于迭代一组值。没有更多的值可供迭代时，方法__next__应引发StopIteration异常。
可迭代对象包含方法__iter__，它返回一个像序列一样可用于for循环中的迭代器。通常，迭代器也是可迭代的，即包含返回迭代器本身的方法__iter__。

生成器：生成器的函数是包含关键字yield的函数，它在被调用时返回一个生成器，即一种特殊的迭代器。要与活动的生成器交互，可使用方法send、throw和close。


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

# property类: 新式类通过存取方法定义的属性通常称为特性.
"""
如果特性的行为怪异，务必确保你使用的是新式类（通过直接或间接地继承object或直
接设置__metaclass__）。不然，特性的获取方法依然正常，但设置方法可能不正常（是否
如此取决于使用的Python版本）。这可能有点令人迷惑
"""


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


r = Rectangle()
r.width, r.height = 10, 5
print(r.size)
r.size = 150, 100
print(r.width)


# staticmethod: 静态方法的定义中没有参数self，可直接通过类来调用.
# classmethod: 定义中包含类似于self的参数，通常被命名为cls.对于类方法，也可通过对象直接调用，但参数cls将自动关联到类.

# 手动包装
class MyClass:
    def smeth():
        print('This is a static method')

    smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class method of', cls)

    cmeth = classmethod(cmeth)


# 装饰器包装
class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)


MyClass.smeth()
MyClass.cmeth()

"""
__getattribute__(self, name)：在属性被访问时自动调用（只适用于新式类）.
__getattr__(self, name)：在属性被访问而对象没有这样的属性时自动调用.
__setattr__(self, name, value)：试图给属性赋值时自动调用.
__delattr__(self, name)：试图删除属性时自动调用.
相比函数property，这些魔法方法使用起来要棘手些（从某种程度上说，效率也更低）
"""
"""
赋值循环问题： 即便涉及的属性不是size，也将调用方法__setattr__。因此这个方法必须考虑如下两种
情形：如果涉及的属性为size，就执行与以前一样的操作；否则就使用魔法属性__dict__。
__dict__属性是一个字典，其中包含所有的实例属性。之所以使用它而不是执行常规属性
赋值，是因为旨在避免再次调用__setattr__，进而导致无限循环。
"""


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()


# 迭代（iterate）意味着重复多次，就像循环那样。
# 方法__iter__返回一个迭代器，它是包含方法__next__的对象，而调用这个方法时可不提供任何参数.

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

# 通过对可迭代对象调用内置函数iter，可获得一个迭代器.
it = iter([1, 2, 3])
print(next(it))
print(next(it))


# 从迭代器创建序列
class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
print(list(ti))

# 生成器: 包含yield语句的函数都被称为生成器。生成器不是使用return返回一个值，而是可以生成多个值，每次一个.
# 每次使用yield生成一个值后，函数都将冻结，即在此停止执行，等待被重新唤醒。被重新唤醒后，函数将从停止的地方开始继续执行
nested = [[1, 2], [3, 4], [5]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            print(f'开始调用生成器！')
            yield element


for num in flatten(nested):
    print(f'循环一次：num: {num}')

# 生成器推导（也叫生成器表达式): 其工作原理与列表推导相同，但不是创建一个列表（即不立即执行循环），而是返回一个生成器，让你能够逐步执行计算
g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))
print(next(g))

print(sum(i ** 2 for i in range(10)))


# 递归式生成器: 意层嵌套的列表
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))


# 迭代字符串对象
# 请注意，这里没有执行类型检查：我没有检查nested是否是字符串，而只是检查其行为是否类似于字符串，即能否与字符串拼接。
def flatten(nested):
    try:
        # 不迭代类似于字符串的对象：
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten(['foo', ['bar', ['baz']]])))

"""
通用生成器: 生成器由两个单独的部分组成：生成器的函数和生成器的迭代器。生成器的函数
是由def语句定义的，其中包含yield。生成器的迭代器是这个函数返回的结果。用不太准确的话说，这两个实体通常被视为一个，通称为生成器。
"""
"""
外部世界：外部世界可访问生成器的方法send，这个方法类似于next，但接受一个参数（要发送的“消息”，可以是任何对象）。

生成器：在挂起的生成器内部，yield可能用作表达式而不是语句。换而言之，当生成器重新运行时，yield返回一个值——通过send从外部世界发送的值。
如果使用的是next，yield将返回None。请注意，仅当生成器被挂起（即遇到第一个yield）后，使用send（而不是next）才有意义。
要在此之前向生成器提供信息，可使用生成器的函数的参数
"""


def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new


r = repeater(42)
print(next(r))
print(r.send("Hello, world!"))

"""
生成器还包含另外两个方法。
方法throw：用于在生成器中（yield表达式处）引发异常，调用时可提供一个异常类型、一个可选值和一个traceback对象。
方法close：用于停止生成器，调用时无需提供任何参数
"""


# 模拟生成器： 普通函数模拟生成器
# 下面使用普通函数重写了生成器flatten：
def flatten(nested):
    result = []
    try:
        # 不迭代类似于字符串的对象：
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result

# 八皇后问题:

"""
本章介绍的新函数:

函 数                            描 述
iter(obj)                       从可迭代对象创建一个迭代器
next(it)                        让迭代器前进一步并返回下一个元素
property(fget, fset, fdel, doc) 返回一个特性；所有参数都是可选的
super(class, obj)               返回一个超类的关联实例
"""