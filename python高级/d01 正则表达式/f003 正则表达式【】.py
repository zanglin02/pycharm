# []匹配中括号内的任意一个字符
import re
str1 = 'Hello'
str2 = 'hello'
result1 = re.match('[hH]ello', str1)
result2 = re.match('[hH]ello', str2)
print(result1.group(), result2.group())

str3 = '4Hello'
result3 = re.match('[0-9][hH]ell[a-z]', str3)
print(result3.group())

result4 = re.match('[0-35-9]Hello', str3)  # 排除了4匹配不到了
print(result4.group())

# 另外 [*]表示除了[]内的字符都匹配