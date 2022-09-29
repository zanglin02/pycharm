# 匹配单个任意字符   .
import re
result = re.match('.', 'M')
print(result.group())

result = re.match('.', 'Meeting')
print(result.group())

result = re.match('t.o', 'too')
print(result.group())
