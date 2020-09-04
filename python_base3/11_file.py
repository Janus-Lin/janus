"""
janus.python_base3.11_file
~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 文件

版权所有 © 2020
"""

"""
类似于文件的对象：类似于文件的对象是支持read和readline（可能还有write和writelines）等方法的对象。

打开和关闭文件：要打开文件，可使用函数open，并向它提供一个文件名。如果要确保即便发生错误时文件也将被关闭，可使用with语句。

模式和文件类型：打开文件时，还可指定模式，如'r'（读取模式）或'w'（写入模式）。通过在模式后面加上'b'，可将文件作为二进制文件打开，并关闭Unicode编码和换行符替换。

标准流：三个标准流（模块sys中的stdin、stdout和stderr）都是类似于文件的对象，它们实现了UNIX标准I/O机制（Windows也提供了这种机制）。

读取和写入：要从文件或类似于文件的对象中读取，可使用方法read；要执行写入操作，可使用方法write。
  
读取和写入行：要从文件中读取行，可使用readline和readlines；要写入行，可使用writelines。
  
迭代文件内容：迭代文件内容的方法很多，其中最常见的是迭代文本文件中的行，这可通过简单地对文件本身进行迭代来做到。还有其他与较旧Python版本兼容的方法，如使用readlines
"""

"""
值   描 述
'r'  读取模式（默认值）
'w'  写入模式
'x'  独占写入模式
'a'  附加模式
'b'  二进制模式（与其他模式结合使用）
't'  文本模式（默认值，与其他模式结合使用）
'+'  读写模式（与其他模式结合使用）
"""

f = open('data/somefile.txt', 'w')
f.write('Hello, ')
f.write('World!')
f.close()
f = open('data/somefile.txt', 'r')
print(f.read(4))
print(f.read())

# 在这里打开文件
try:
    # 将数据写入到文件中
    f = open('data/somefile.txt', 'w')
    f.write('Hello, \n asdasd')
finally:
    f.close()

# with语句实际上是一个非常通用的结构，允许你使用所谓的上下文管理器。上下文管理器是支持两个方法的对象：__enter__和__exit__。
# 方法__enter__不接受任何参数，在进入with语句时被调用，其返回值被赋给关键字as后面的变量。返回文件对象本身.
# 方法__exit__接受三个参数：异常类型、异常对象和异常跟踪。关闭文件.
print('-' * 20)

f = open(r'data/somefile.txt')

# read(n)
print(f.read(7))

# read()
print(f.read())

# readline()
for i in range(3):
    print(str(i) + ': ' + f.readline(), end='')

# readlines()
print(f.readlines())

# 写入文件后将其关闭，以确保数据得以写入磁盘. 
f.close()


# 使用read遍历字符
def process(string):
    print('Processing:', string)


filename = r'data/somefile.txt'
with open(filename) as f:
    char = f.read(1)
    while char:
        process(char)
        char = f.read(1)

# 在while循环中使用readline
with open(filename) as f:
    while True:
        line = f.readline()
        if not line: break
        process(line)

# 模块fileinput会负责打开文件，你只需给它提供一个文件名即可
import fileinput

for line in fileinput.input(filename):
    process(line)

# 最常见的文件迭代器
with open(filename) as f:
    for line in f:
        process(line)
