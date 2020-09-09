"""
janus.python_base3.08_exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 异常

版权所有 © 2020
"""
# 异常： 异常情况（如发生错误）是用异常对象表示的。对于异常情况，有多种处理方式；如果忽略，将导致程序终止。
# 注意到异常处理并不会导致代码混乱，而添加大量的if语句来检查各种可能的错误状态将导致代码的可读性极差.

# raise: 要引发异常，可使用raise语句，并将一个类（必须是Exception的子类）或实例作为参数。将类作为参数时，将自动创建一个实例。
# raise Exception('hyperdrive overload')
"""
一些内置的异常类
类 名                描 述
Exception           几乎所有的异常类都是从它派生而来的
AttributeError      引用属性或给它赋值失败时引发
OSError             操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
IndexError          使用序列中不存在的索引时引发，为LookupError的子类
KeyError            使用映射中不存在的键时引发，为LookupError的子类
NameError           找不到名称（变量）时引发
SyntaxError         代码不正确时引发
TypeError           将内置操作或函数用于类型不正确的对象时引发
ValueError          将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
ZeroDivisionError   在除法或求模运算的第二个参数为零时引发
"""

"""
自定义的异常类:
要捕获异常，可在try语句中使用except子句。在except子句中，如果没有指
定异常类，将捕获所有的异常。你可指定多个异常类，方法是将它们放在元组中。如果
向except提供两个参数，第二个参数将关联到异常对象。在同一条try/except语句中，可
包含多个except子句，以便对不同的异常采取不同的措施。
"""


class SomeCustomException(Exception): pass


# 捕获异常: 异常比较有趣的地方是可对其进行处理，通常称之为捕获异常.
# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
#     print(x / y)
# except ZeroDivisionError:
#     print("The second number can't be zero!")


# 可以用if替换, 而使用try/except的话只需要一个错误处理程序，不用没一个数都检测.

# 抑制异常: 发生除零行为时，如果启用了“抑制”功能，方法calc将（隐式地）返回None。换而言之，如果启用了“抑制”功能，就不应依赖返回值。
class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise


calculator = MuffledCalculator()
calculator.calc('10 / 2')

calculator.muffled = True
calculator.calc('10 / 0')

# 你可使用raise ... from ...语句来提供自己的异常上下文，也可使用None来禁用上下文.
# try:
#     1 / 0
# except ZeroDivisionError:
#     raise ValueError from None

# 多个 except 子句: 防止漏网之鱼
try:
    1 / 0
except ZeroDivisionError:
    print("The second number can't be zero!")
except TypeError:
    print("That wasn't a number, was it?")

# 一箭双雕: 使用一个except子句捕获多种异常，可在一个元组中指定这些异常.
try:
    1 / 0
except (ZeroDivisionError, TypeError, NameError):
    print('Your numbers were bogus ...')

# 捕获对象: 要在except子句中访问异常对象本身，可使用两个而不是一个参数。
try:
    '' / 0
except (ZeroDivisionError, TypeError) as e:
    print(f'捕获对象: {e}')

# 一网打尽: 是要使用一段代码捕获所有的异常，只需在except语句中不指定任何异常类即可。
try:
    '' / ''
except:
    print('Something wrong happened ...')

# 万事大吉: 使用except Exception as 捕获所有异常.
# while True:
#     try:
#         1 / 0
#     except Exception as e:
#         print('Invalid input:', e)
#         print('Please try again')
#     else:
#         break

# 最后一招： finally： 不管try子句中发生什么异常，都将执行finally子句. 非常适合用于确保文件或网络套接字等得以关闭.
# else子句：除except子句外，你还可使用else子句，它在主try块没有引发异常时执行。
try:
    1 / 1
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Finally")


# 不处理异常： 引发一条栈跟踪消息, 异常将继续传播，直至到达主程序（全局作用域）.

# 基础
def describe_person(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    if 'occupation' in person:
        print('Occupation:', person['occupation'])


# 异常优化
def describe_person(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    try:
        print('Occupation:', person['occupation'])
    except KeyError:
        pass


# 检查对象是否包含特定的属性时，try/except也很有用
obj = ''
try:
    obj.write
except AttributeError:
    print('The object is not writeable')
else:
    print('The object is writeable')

# 不那么异常的情况： 你只想发出警告，指出情况偏离了正轨，可使用模块warnings中的函数warn.
from warnings import warn

warn("I've got a bad feeling about this.")

# 可使用模块warnings中的函数filterwarnings来抑制你发出的警告（或特定类型的警告），并指定要采取的措施，如"error"或"ignore"
from warnings import filterwarnings

# filterwarnings("ignore")
# warn("Anyone out there?")
# filterwarnings("error")
# warn("Something is very wrong!")

"""
函数                                                     描述
warnings.filterwarnings(action,category=Warning, ...)   用于过滤警告
warnings.warn(message, category=None)                   用于发出警告
"""
