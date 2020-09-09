"""
janus.util
~~~~~~~~~~

功能: 文本块生成器

版权所有 © 2020
"""


def lines(file):
    """在文件末尾添加一个空行"""
    for line in file: yield line
    yield '\n'


def blocks(file: object) -> object:
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
