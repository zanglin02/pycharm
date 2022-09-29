# | 匹配符号左右两边任意一个表达式
# 在列表中匹配多个字符串

import re
fruit_list = ['apple', 'orange', 'banana', 'mango']
for value in fruit_list:
    result = re.match('apple|banama', value)
    if result:
        print(f'{result.group()}是我想要的')
    else:
        print(f'{value}不是我想要的')
