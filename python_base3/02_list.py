"""
janus.python_base3.02_list
~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 列表元组

版权所有 © 2020, 美通智投（北京）科技有限公司
"""

"""
Python支持一种数据结构的基本概念，名为容器（container）。容器基本上就是可包含其他对象的对象。两种主要的容器是序列（如列表和元组）和映射（如字典）。

序列：一种数据结构，其中的元素带编号（编号从0开始）。
列表、字符串和元组都属于序列，其中列表是可变的（你可修改其内容），
元组和字符串是不可变的（一旦创建，内容就是固定的）。
有几种操作适用于所有序列，包括索引、切片、相加、相乘和成员资格检查。
"""


"""
索引（indexing）:序列中的所有元素都有编号——从0开始递增。你可像下面这样使用编号来访问各个元素,
你可使用索引来获取元素。这种索引方式适用于所有序列。当你使
用负数索引时，Python将从右（即从最后一个元素）开始往左数，因此1是最后一个元素的位置
"""
lst_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst_index[0])


"""
序列：通用操作
切片（slicing）: 除使用索引来访问单个元素外，还可使用切片（slicing）来访问特定范围内的元素。为此，
可使用两个索引，并用冒号分隔：简而言之，你提供两个索引来指定切片的边界，其中第一个索引指定的元素包含在切片内，
但第二个索引指定的元素不包含在切片内.

步长: 执行切片操作时，你显式或隐式地指定起点和终点，但通常省略另一个参数，即步长。在普通切片中，步长为1。
这意味着从一个元素移到下一个元素，因此切片包含起点和终点之间的所有元素。

拼接： 同类型数据结构可使用加法运算符来拼接序列。 将序列与数x相乘时，将重复这个序列x次来创建一个新序列
      
None、空列表和初始化
空列表: 是使用不包含任何内容的两个方括号（[]）表示的.
None表示什么都没有。因此，要将列表的长度初始化为10.
"""

print(lst_index[1:4])
print(lst_index[-3:])
print(lst_index[1:6:2])
print(lst_index[::2])
print(lst_index[10:0:-2])
print([1, 2] + [3, 4])
print([1, 2] * 2)

"""
list： 操作
成员资格: 要检查特定的值是否包含在序列中，可使用运算符in。
内置函数len、min和max很有用，其中函数len返回序列包含的元素个数，而min和max分别返
回序列中最小和最大的元素

列表:是可变的，即可修改其内容。类list: 可将任何序列（而不仅仅是字符串）作为list的参数。

删除元素: 删除元素
切片赋值: 通过使用切片赋值，可将切片替换为长度与其不同的序列.在不替换原有元素的情况下插入新元素
追加：append
清空：clear
复制：copy
统计： 方法count计算指定的元素在列表中出现了多少次。
多个值追加： 方法extend让你能够同时将多个值附加到列表末尾，为此可将这些值组成的序列作为参数提供给方法extend。换而言之，你可使用一个列表来扩展另一个列表。
index： 方法index在列表中查找指定值第一次出现的索引
insert： 方法insert用于将一个对象插入列表
pop： 方法pop从列表中删除一个元素（末尾为最后一个元素），并返回这一元素，pop是唯一既修改列表又返回一个非None值的列表方法
push和pop是大家普遍接受的两种栈操作（加入和取走）的名称。Python没有提供push，但可使用append来替代。
方法pop和append的效果相反，因此将刚弹出的值压入（或附加）后，得到的栈将与原来相同。

remove: 方法remove用于删除第一个为指定值的元素.
reverse: 方法reverse按相反的顺序排列列表中的元素（我想你对此应该不会感到惊讶）.如果要按相反的顺序迭代序列，可使用函数reversed。

sort: 方法sort用于对列表就地排序①。就地排序意味着对原来的列表进行修改，使其元素按顺序排列，而不是返回排序后的列表的副本
高级排序: 方法sort接受两个可选参数：key和reverse。 (函数sorted也接受参数key和reverse)
"""


"""

元组：不可修改的序列, 如何表示只包含一个值的元组呢？这有点特殊：虽然只有一个值，也必须在它后面加上逗号. 
元组的创建及其元素的访问方式与其他序列相同

元组与列表区别：
它们用作映射中的键（以及集合的成员），而列表不行。映射将在第4章详细介绍。

有些内置函数和方法返回元组，这意味着必须跟它们打交道。只要不尝试修改元组，与元组“打交道”通常意味着像处理列表一样处理它们
（需要使用元组没有的index和count等方法时例外）
"""

sequence = [None] * 10
print(sequence)
print(max('212124'))
print(list('123456'))
print(''.join(['1', '2', '3', '4', '5', '6']))
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)
names[2:] = list('21212')
print(names)
names[1:1] = [2, 3, 4]
print(names)
names[1:4 ] = []
print(names)

names.append(4)
names.clear()
a = names.copy()
b = names.count(1)
print(names)
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))
knights.insert(3, 'four')
print(knights)

x = [1, 2, 3]
x.pop()
print(x)

x.append(x.pop())
print(x)

x.remove(2)
print(x)
b.reverse()
print(b)

x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)
print(sorted('Python'))

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)     # 按长度排序
print(x)
x.sort(reverse=False)    # 排序方向
print(x)
print(tuple('abc'))