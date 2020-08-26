"""
janus.python_base3.06_abstract
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 抽象-函数

版权所有 © 2020
"""


# 抽象：程序能够被人理解, 抽象是隐藏不必要细节的艺术。通过定义处理细节的函数，可让程序更抽象.

# 文档字符串（docstring）
def square(x):
    'Calculates the square of the number x.'
    return x * x


print(square.__doc__)
print(help(square))


# 收集参数: 星号不会收集关键字参数
def print_params(a, *params):
    print(params)


print_params(1, 2, 3)


# 要收集关键字参数，可使用两个星号
def print_params_3(**params):
    print(params)


print_params_3(x=1, y=2, z=3)


# 分配参数:
def hello_3(greeting='Hello', name='world'):
    print('{}, {}!'.format(greeting, name))


params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)

# 命名空间/作用域: 变量到底是什么呢？可将其视为指向值的名称。因此，执行赋值语句x = 1后，名称x指向值1。这几乎与使用字典时一样（字典中的键指向值），只是你使用的是“看不见”的字典。
# 函数内部作用域(局部命名空间）改变时，不影响外部（全局）作用域内同名变量。

# 重新关联： 联全局变量（使其指向新值）是另一码事。在函数内部给变量赋值时，该变量默认为局部变量，除非你明确地告诉Python它是全局变量。
x = 1


def change_global():
    global x
    x = x + 1


change_global()
print(x)


# 闭包: 一个函数位于另一个函数中，且外面的函数返回里面的函数
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor

    return multiplyByFactor


double = multiplier(2)
print(double(5))

triple = multiplier(3)
print(triple(3))

print(multiplier(5)(4))


# 递归：递归意味着引用（这里是调用）自身
# 基线条件（针对最小的问题）：满足这种条件时函数将直接返回一个值
# 递归条件：包含一个或多个调用，这些调用旨在解决问题的一部分。

# 阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))


# 幂：原始版本
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


# 幂：递归
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

# 二分查找： 关键在于元素是经过排序的
# 实际上，模块bisect提供了标准的二分查找实现
def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
    if number > sequence[middle]:
        return search(sequence, number, middle + 1, upper)
    else:
        return search(sequence, number, lower, middle)


print(search([0,1, 2, 3, 4, 5, 6, 7, 8], 6, 0, 7))

# 函数式编程
# map:对序列中的所有元素执行函数
print(list(map(str, range(10))))

# 等价于
print([str(i) for i in range(10)])

# filter: 返回一个列表，其中包含对其执行函数时结果为真的所有元素
def func(x):
    return x.isalnum()
seq = ["foo", "x41", "?!", "***"]
print(list(filter(func, seq)))

# 等价于, 列表推到式
print([x for x in seq if x.isalnum()])

# 等价宇， lambda(匿名函数)
print(filter(lambda x: x.isalnum(), seq))

# reduce: 使用指定的函数将序列的前两个元素合二为一，再将结果与第3个元素合二为一，依此类推，直到处理完整个序列并得到一个结果
# 就这个示例而言，还不如使用内置函数sum
numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
print(reduce(lambda x, y: x + y, numbers))
print(sum(numbers))

"""
本章介绍的新函数
函 数                          描 述
map(func, seq[, seq, ...])    对序列中的所有元素执行函数
filter(func, seq)             返回一个列表，其中包含对其执行函数时结果为真的所有元素
reduce(func, seq[, initial])  等价于 func(func(func(seq[0], seq[1]), seq[2]), ...)
sum(seq)                      返回 seq 中所有元素的和
apply(func[, args[, kwargs]]) 调用函数（还提供要传递给函数的参数）
"""