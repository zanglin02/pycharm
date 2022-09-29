# ^ 匹配字符串开头
# $ 匹配字符串结尾
import re
# 匹配以数字开头的数据
result = re.match('^\d.*\s', '4hello world!')
if result:
    print(result.group())
else:
    print('匹配失败')

# 匹配以数字结尾
result = re.match('.*\d$', 'hello world!5')
if result:
    print(result.group())
else:
    print('匹配失败')

# 数字开头数字结尾
result = re.match('^\d.*\d$', '4hello4')
if result:
    print(result.group())
else:
    print('匹配失败')

