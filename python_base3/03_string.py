"""
janus.python_base3.03_string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

功能: 字符串

版权所有 © 2020,
"""
import string


# ------------------------模块string中几个很有用的常量------------------------------
# 包含数字0～9的字符串
print(string.digits)

# 包含所有ASCII字母（大写和小写）的字符串
print(string.ascii_letters)

# 包含所有小写ASCII字母的字符串
print(string.ascii_lowercase)

# 包含所有可打印的ASCII字符的字符串
print(string.printable)

# 包含所有ASCII标点字符的字符串
print(string.punctuation)

# 包含所有大写ASCII字母的字符串
print(string.ascii_uppercase)

# -------------------------------字符串方法---------------------------------------
#  center: 两边添加填充字符（默认为空格）让字符串居中'i love you'.center(2, "*")
print('i love you'.center(39, "*"))

# find：在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。
# 附录B：rfind、index、rindex、count、startswith、endswith。
title = "Monty Python's Flying Circus"
print(title.find('Python'))

# join： 是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素。
seq = ['1', '2', '3', '4', '5']
print('-'.join(seq))

# lower: 返回字符串的小写版本。解决方案是在存储和搜索时
# islower、istitle、isupper、translate, capitalize、casefold、swapcase、title、upper
print('Trondheim'.lower())
print("that's all, folks".title()) # 首字母大写
print(string.capwords("that's all, folks")) # 更好点

# replace： 将指定子串都替换为另一个字符串，并返回替换后的结果
print('This is a test'.replace('is', 'eez') )

# split： 一个非常重要的字符串方法，其作用与join相反，用于将字符串拆分为序列。
# partition、rpartition、rsplit、splitlines
print( '1+2+3+4+5'.split('+') )

# strip： 将字符串开头和末尾的空白（但不包括中间的空白）删除，并返回删除后的结果。
# 应用场景：用户输入用户名时不小心在末尾加上了一个空格
print(' internal whitespace is kept '.strip())
print('×××internal whitespace is kept×××'.strip("×"))

# translate： 与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。这个方法的优势在于能够同时替换多个字符，因此效率比replace高
# 使用translate前必须创建一个转换表，长度相同的字符串，对应替换。,提供可选的第三个参数指定要将哪些字母删除
table = str.maketrans('cs', 'kz')
print('this is an incredible test'.translate(table))
table = str.maketrans('cs', 'kz', ' ')
print('this is an incredible test'.translate(table))

# 判断字符串是否满足特定的条件
# isalnum、isalpha、isdecimal、isdigit、isidentifier、islower、isnumeric、isprintable、isspace、istitle、isupper。

"""
本章介绍的新函数
函 数                                描 述
string.capwords(s[, sep])           使用split根据sep拆分s，将每项的首字母大写，再以空格为分隔符将它们合并起来
ascii(obj)                          创建指定对象的ASCII表示
"""