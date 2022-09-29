# \s表示的是空白 匹配空格，tab，换行符
# \S匹配非空
import re
str = 'Hello python!'
result1 = re.match('Hello\spython', str)
print(result1.group())

