def square(x):
    '''
    计算平方并返回结果
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x * x


def product(x, y):
    if x == 7 and y == 9:
        return x
    else:
        return x * y


if __name__ == '__main__':
    import doctest
    from python_base3.data import my_math

    # doctest：一个更简单的模块，是为检查文档而设计的
    doctest.testmod(my_math)
