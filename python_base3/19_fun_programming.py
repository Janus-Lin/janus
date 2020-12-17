"""
janus.python_base3.19_fun_programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 灵活性, 原型设计, 配置, 日志

版权所有 © 2020
"""
"""
灵活性： 设计和编程时，应以灵活性为目标。随着对所面临问题了解得越来越深入，你应心甘情愿乃至随时准备修改程序的方方面面，不要固守最初的想法。

原型设计： 要深入了解问题和可能的实现方案，一个重要的技巧是编写程序的简化版本，以了解它是如何工作的。使用Python编写原型非常容易，使用众多其他语言编写一个原型
所需的时间足以让你用Python编写多个原型。即便如此，除非万不得已，否则不要推倒重来，因为重构通常是更佳的解决方案。

配置：通过提取程序中的常量，可让以后修改程序变得更容易。通过将这些常量放在配置文件中，让用户能够配置程序，使其按自己希望的方式行事。
通过使用环境变量和命令行选项，可进一步提高程序的可配置性。提取代码中的符号常量.

日志： 日志对找出程序存在的问题或监视其行为大有裨益。你可自己动手使用print语句实现简单的日志，但最安全的做法是使用标准库中的模块logging
"""
# 原型（prototype）指的是尝试性实现，即一个模型。它实现了最终程序的主要功能，但在后期可能需要重写，也可能不用重写。通常，最初的原型都能变成可行的程序.


from configparser import ConfigParser

# 读取配置文件
CONFIGFILE = "area.ini"
config = ConfigParser()
# 读取配置文件：
config.read(CONFIGFILE)
# 打印默认问候语（greeting）：
# 在messages部分查找问候语：
print(config['messages'].get('greeting'))
# 使用配置文件中的提示（question）让用户输入半径：
radius = float(input(config['messages'].get('question') + ' '))
# 打印配置文件中的结果消息（result_message）；
# 以空格结束以便接着在当前行打印：
print(config['messages'].get('result_message'), end=' ')
# getfloat()将获取的值转换为浮点数：
print(config['numbers'].getfloat('pi') * radius ** 2)

"""
01-记录不同类型的条目（信息、调试信息、警告、自定义类型等）。默认情况下，只记录警告。（这就是我在代码清单19-3中显式地将level设置为logging.INFO的原因所在。）

02-只记录与程序特定部分相关的条目。

03-记录有关时间、日期等方面的信息。

04-记录到其他位置，如套接字。

05-配置日志器，将一些或大部分日志过滤掉，这样无需重写程序就能获得所需的日志信息。模块logging非常复杂，文档中还提供了其他很多相关的信息
"""
import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')
print(1 / 0)
logging.info('The division succeeded')
logging.info('Ending program')

