"""
janus.python_base3.01_basic framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 基础框架概览

版权所有 © 2020, lin
"""

"""
程序：算法 + 数据结构
算法：算法犹如菜谱，告诉你如何完成特定的任务。从本质上说，编写计算机程序就是使用计算机能够理解的语言（如Python）描述一种算法.
这种对机器友好的描述被称为程序，主要由表达式和语句组成。
"""

"""
表达式：表达式为程序的一部分，结果为一个值。例如，2 + 2就是一个表达式，结果为4。简单表达式是使用运算符（如+或%）和函数（如pow）
将字面值（如2或"Hello"）组合起来得到的。通过组合简单的表达式，可创建复杂的表达式，如(2 + 2) *(3 - 1)。表达式还可能包含变量.
表达式=运算符+数（有进制）,但既不会将结果保存起来，也不会向用户显示它.
"""

"""
变量：变量是表示值的名称。通过赋值，可将新值赋给变量，如x = 2。赋值是一种语句。使用Python变量前必须给它赋值，因为Python变量没有默认值.
nan具有特殊含义，指的是“非数值”（not a number）
"""

"""
语句：语句是让计算机执行特定操作的指示。这种操作可能是修改变量（通过赋值）、将信息打印到屏幕上（如print("Hello, world!")）、
导入模块或执行众多其他任务。根本特征：执行修改操作。
"""

"""
函数：Python函数类似于数学函数，它们可能接受参数，并返回结果（犹如小型程序，可用来执行特定的操作）
还有一些类似的函数，可用于转换类型，如str和float。实际上，它们并不是函数，而是类。
"""

"""
模块：模块是扩展，可通过导入它们来扩展Python的功能。例如，模块math包含多个很有用的函数
"""

"""
标识符: 在Python中，名称（标识符）只能由字母、数字和下划线（_）构成，且不能以数字打头。 因此Plan9是合法的变量名，而9Plan不是
"""

"""
字符串：字符串非常简单。它们其实就是一段文本，其中的字符是用Unicode码点表示的。然而，对于字符串，需要学习的知识有很多。
原始字符串用前缀r表示。看起来可在原始字符串中包含任何字符，这大致是正确的。
"""
print(r'C:\nowhere')

# Python还提供了bytearray，它是bytes的可变版。从某种意义上说，它就像是可修改的字符串——常规字符串是不能修改的。
x = bytearray(b"Hello!")
x[1] = ord(b"u")
print(x)

"""
本章介绍的新函数
函 数                                描 述
abs(number)                         返回指定数的绝对值
bytes(string, encoding[, errors])   对指定的字符串进行编码，并以指定的方式处理错误
cmath.sqrt(number)                  返回平方根；可用于负数
float(object)                       将字符串或数字转换为浮点数
help([object])                      提供交互式帮助
input(prompt)                       以字符串的方式获取用户输入
int(object)                         将字符串或数转换为整数
math.ceil(number)                   以浮点数的方式返回向上圆整的结果
math.floor(number)                  以浮点数的方式返回向下圆整的结果
math.sqrt(number)                   返回平方根；不能用于负数
pow(x, y[, z])                      返回x的y次方对z求模的结果
print(object, ...)                  将提供的实参打印出来，并用空格分隔
repr(object)                        返回指定值的字符串表示
round(number[, ndigits])            四舍五入为指定的精度，正好为5时舍入到偶数
str(object)                         将指定的值转换为字符串。用于转换bytes时，可指定编码和错误处理方式
"""
