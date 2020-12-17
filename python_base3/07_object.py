"""
janus.python_base3.object
~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 对象

版权所有 © 2020
"""
from abc import ABC, abstractmethod

# 对象:大致意味着一系列数据（属性）以及一套访问和操作这些数据的方法.
"""
多态：多态指的是能够同样地对待不同类型和类的对象，即无需知道对象属于哪个类就可调用其方法

封装：对象可能隐藏（封装）其内部状态。在有些语言中，这意味着对象的状态（属性）只能通过其方法来访问。在Python中，所有的属性都是公有的，但直接访问对象的状态时程序员应谨慎行事，因为这可能在不经意间导致状态不一致

继承：一个类可以是一个或多个类的子类，在这种情况下，子类将继承超类的所有方法。你可指定多个超类，通过这样做可组合正交（独立且不相关）的功能。为此，一种常见的做法是使用一个核心超类以及一个或多个混合超类
"""
# 多态
print('abc'.count('a'))
print([1, 2, 'a'].count('a'))


# 类：类表示一组（或一类）对象，而每个对象都属于特定的类。类的主要任务是定义其实例将包含的方法。
# self： 甚至必不可少。所有的方法都访问对象本身——要操作的属性所属的对象。
# 对象由属性和方法组成。属性不过是属于对象的变量，而方法是存储在属性中的函数。相比于其他函数，（关联的）方法有一个不同之处，那就是它总是将其所属的对象作为第一个参数，而这个参数通常被命名为self。
class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))


# 私有化：要让方法或属性成为私有的（不能从外部访问），只需让其名称以两个下划线打头即可。
"""
如果你不希望名称被修改，又想发出不要从外部修改属性或方法的信号，可用一个下划线打
头。这虽然只是一种约定，但也有些作用。例如，from module import *不会导入以一个下划线
打头的名称
"""


class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me ...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


s = Secretive()

# 直接访问私有方法, 会报错
# s.__inaccessible()

# 通过特殊方式访问私有方法
s._Secretive__inaccessible()


# 定义类时情况亦如此：在class语句中定义的代码都是在一个特殊的命名空间（类的命名空间）内执行的，而类的所有成员都可访问这个命名空间。
# 类定义其实就是要执行的代码段
def foo(x):
    return x * x


foo = lambda x: x * x

"""
请注意SPAMFilter类的定义中有两个要点。
以提供新定义的方式重写了Filter类中方法init的定义。
直接从Filter类继承了方法filter的定义，因此无需重新编写其定义。
"""

class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):  # SPAMFilter是Filter的子类
    def init(self):  # 重写超类Filter的方法init

        self.blocked = ['SPAM']


# 要确定一个类是否是另一个类的子类，可使用内置方法issubclass
print(issubclass(SPAMFilter, Filter))

# 如果你有一个类，并想知道它的基类，可访问其特殊属性__bases_
print(SPAMFilter.__bases__)

# 要确定对象是否是特定类的实例，可使用isinstance
s = SPAMFilter()
print(isinstance(s, SPAMFilter))

# 如果你要获悉对象属于哪个类，可使用属性__class__。
print(s.__class__)


# 多重继承
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk()

# 并发症:多个超类的超类相同时，查找特定方法或属性时访问超类的顺序称为方法解析顺序（MRO）
# 如果多个超类以不同的方式实现了同一个方法（即有多个同名方法），必须在class语句中小心排列这些超类，因为位于前面的类的方法将覆盖位于后面
# 的类的方法。因此，在前面的示例中，如果Calculator类包含方法talk，那么这个方法将覆盖Talker
# 类的方法talk（导致它不可访问）。如果像下面这样反转超类的排列顺序class TalkingCalculator(Talker, Calculator): pass

# 接口: 这一概念与多态相关。处理多态对象时，你只关心其接口（协议）——对外暴露的方法和属性
# 是检查所需的方法是否存在
print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))

# 检查属性talk是否是可调用的
print(callable(getattr(tc, 'talk', None)))
print(callable(getattr(tc, 'fnord', None)))

# 这里没有在if语句中使用hasattr并直接访问属性，而是使用了getattr（它让我能够指定属性不存在时使用的默认值，这里为None），然后对返回的对象调用callable。

# setattr与getattr功能相反，可用于设置对象的属性：
setattr(tc, 'name', 'Mr. Gumby')
print(tc.name)

# 查看对象中存储的所有值
print(tc.__dict__)

# 抽象基类： 使用模块abc可创建抽象基类。抽象基类用于指定子类必须提供哪些功能，却不实现这些功能


class Talker(ABC):
    @abstractmethod  # 标记为抽象的——在子类中必须实现的方法。
    def talk(self):
        pass


# Talker(): 实例化会报错。继承+重写，可以调用

class Knigget(Talker):
    def talk(self):
        print("Ni!")


k = Knigget()
print(isinstance(k, Talker))
print(k.talk())

# 鸭子类型： 继承+重写方法。不关心对象是什么，只关心对象能做什么（它实现了哪些方法）
# 类的注册：Talker.register(Herring)

"""
面向对象设计的一些思考

01-将相关的东西放在一起。如果一个函数操作一个全局变量，最好将它们作为一个类的属性和方法.

02-不要让对象之间过于亲密。方法应只关心其所属实例的属性，对于其他实例的状态，让它们自己去管理就好了.

03-慎用继承，尤其是多重继承。继承有时很有用，但在有些情况下可能带来不必要的复杂性。要正确地使用多重继承很难，要排除其中的bug更难.

04-保持简单。让方法短小紧凑。一般而言，应确保大多数方法都能在30秒内读完并理解。对于其余的方法，尽可能将其篇幅控制在一页或一屏内.
"""

"""
命名规则：

(1) 将有关问题的描述（程序需要做什么）记录下来，并给所有的名词、动词和形容词加上标记.
(2) 在名词中找出可能的类.
(3) 在动词中找出可能的方法.
(4) 在形容词中找出可能的属性.
(5) 将找出的方法和属性分配给各个类.
"""

"""
面向对象模型:
(1) 记录（或设想）一系列用例，即使用程序的场景，并尽力确保这些用例涵盖了所有的功能。
(2) 透彻而仔细地考虑每个场景，确保模型包含了所需的一切。如果有遗漏，就加上；如果有不太对的地方，就修改。不断地重复这个过程，直到对模型满意为止
"""

"""
本章介绍的新函数
函 数                           描 述
callable(object)               判断对象是否是可调用的（如是否是函数或方法）
getattr(object,name[,default]) 获取属性的值，还可提供默认值
hasattr(object, name)          确定对象是否有指定的属性
isinstance(object, class)      确定对象是否是指定类的实例
issubclass(A, B)               确定A是否是B的子类
random.choice(sequence)        从一个非空序列中随机地选择一个元素
setattr(object, name, value)   将对象的指定属性设置为指定的值
type(object)                   返回对象的类型
"""
