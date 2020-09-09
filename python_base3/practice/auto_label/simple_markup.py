import sys, re
from python_base3.practice.auto_label.util import *

# python simple_markup.py < test_input.txt > test_output.html
print('<html><head><title>...</title><body>')
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')
