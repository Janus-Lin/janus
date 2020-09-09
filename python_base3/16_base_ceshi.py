"""
janus.python_base3.16_base_ceshi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 测试基础, 测试用例, 代码检测, 性能分析

版权所有 © 2020
"""
"""
测试驱动编程： 大致而言，测试驱动编程意味着先测试再编码。有了测试，你就能信心满满地修改代码，这让开发和维护工作更加灵活。

模块doctest和unittest： 需要在Python中进行单元测试时，这些工具必不可少。模块doctest设计用于检查文档字符串中的示例，但也可轻松地使用它来设计测试套件。
为让测试套件更灵活、结构化程度更高，框架unittest很有帮助。

PyChecker和PyLint： 这两个工具查看源代码并指出潜在（和实际）的问题。它们检查代码的方方面面——从变量名太短到永远不会执行的代码段。
你只需编写少量的代码，就可将它们加入测试套件，从而确保所有修改和重构都遵循了你采用的编码标准。

性能分析：如果你很在乎速度，并想对程序进行优化（仅当绝对必要时才这样做），应首先进行性能分析：使用模块profile或cProfile来找出代码中的瓶颈.
"""
"""
函 数                         描 述
doctest.testmod(module)      检查文档字符串中的示例（还接受很多其他的参数）
unittest.main()              运行当前模块中的单元测试
profile.run(stmt[,filename]) 执行语句并对其进行性能分析；可将分析结果保存到参数filename指定的文件中
"""
# 需求说明(开发文档): 开发软件时，必须先知道软件要解决什么问题——要实现什么样的目标。要阐明程序的目标。
from python_base3.data import area

# 简单的测试程序
# 先编写测试再编写代码并不是为了发现bug，而是为了检查代码是否管用。这有点像古老的禅语所说：如果没有人听到，就认为森林中的树木倒下时没有发出声音吗？
height = 3
width = 4
correct_answer = 12
answer = area.rect_area(height, width)
if answer == correct_answer:
    print('Test passed ')
else:
    print('Test failed ')

# 代码覆盖率: 是一个重要的测试概念。运行测试时，测量测试期间实际运行的代码所占的比例.
"""
测试四步曲: 
(1) 确定需要实现的新功能。可将其记录下来，再为之编写一个测试。
(2) 编写实现功能的框架代码，让程序能够运行（不存在语法错误之类的问题, 保证测试框架成功），但测试依然无法通过(确保可以过滤错误，不是一直通过)。
(3) 编写让测试刚好能够通过的代码。在这个阶段，无需完全实现所需的功能，而只要让测试能够通过即可。这样，在整个开发阶段，都能够让所有的测试通过（首次运行测试时除外），即便是刚着手实现功能时亦如此。
(4) 改进（重构）代码以全面而准确地实现所需的功能，同时确保测试依然能够成功。
"""
# 有关模块doctest: data/my_math.py
# 标准库包含另外两个有趣的单元测试工具：pytest（pytest.org）和nose（nose.readthed ocs.io）

# unittest: janus/python_base3/16_base_ceshi.py
# 测试夹具: 方法setUp和tearDown，它们将分别在每个测试方法之前和之后执行。你可使用这些方法来执行适用于所有测试的初始化代码和清理代码.
# 模块unittest区分错误和失败。错误指的是引发了异常，而失败是调用failUnless等方法的结果.
# 开头的两个句点表示测试。如果你仔细观察失败时乱七八糟的输出，将发现开头也有两个字符：两个F，表示两次失败.
# 有关更复杂的面向对象代码测试，请参阅模块unittest.mock。


# 源代码检查(PyChecker): 感觉可以用pycharm重新格式优化和makefile文件代替.
# 标准库还包含一个名为timeit的模块，提供了一种对小段Python代码的运行时间进行测试的简单方式.
# 性能分析： profile, 可以用pycharm的性能调试代替模块检测.
import cProfile
from python_base3.data.my_math import product
cProfile.run('product(1, 2)', 'my_math.profile')
import pstats
p = pstats.Stats('my_math.profile')