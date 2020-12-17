"""
janus.python_base3.17_python_extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: python扩展

版权所有 © 2020
"""
"""
扩展理念： Python扩展的主要用途有两个——利用既有（遗留）代码和提高瓶颈部分的速度。从头开始编写代码时，请尝试使用Python建立原型，
找出其中的瓶颈并在需要时使用扩展来替换它们。预先将潜在的瓶颈封装起来大有裨益。

Jython和IronPython： 对这些Python实现进行扩展很容易，使用底层语言（对于Jython，为Java；对于IronPython，
为C#和其他.NET语言）以库的方式实现扩展后，就可在Python中使用它们了。

扩展方法： 有很多用于扩展代码或提高其速度的工具，有的让你更轻松地在Python程序中嵌入C语言代码，有的可提高数字数组操作等常见运算的速度，
有的可提高Python本身的速度。这样的工具包括SWIG、Cython、Weave、NumPy、ctypes和subprocess。

SWIG： SWIG是一款自动为C语言库生成包装代码的工具。包装代码自动处理Python CAPI，使你不必自己去做这样的工作。
使用SWIG是最简单、最流行的扩展Python的方式之一。

使用Python/C API： 可手工编写可作为共享库直接导入到Python中的C语言代码。为此，必须遵循Python/C API：对于每个函数，
你都需要负责完成引用计数、提取参数以及创建返回值等工作；另外，还需编写将C语言库转换为模块的代码，包括列出模块中的函数以及创建模块初始化函数。
"""
"""
函 数                             描 述
Py_INCREF(obj)                   将obj的引用计数加1
Py_DECREF(obj)                   将obj的引用计数减1
PyArg_ParseTuple(args, fmt, ...) 提取位置参数
PyArg_ParseTupleAndKeywords(args, kws, fmt, kwlist) 提取位置参数和关键字参数
PyBuildValue(fmt, value)         根据C语言值创建PyObject
"""

"""
提升速度的情形:
(1) 使用Python开发原型（有关原型开发的详细信息，请参阅第19章）。
(2) 对程序进行性能分析以找出瓶颈（有关测试，请参阅第16章）。
(3) 使用C（或者C++、C#、Java、Fortran等）扩展重写瓶颈部分。
"""
