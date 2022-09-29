# \d 匹配任意数字
# \D 匹配任意非数字
import re
str1 = '我喝过5种口味的元气森林'
result1 = re.match('我喝过\d种口味', str1)
print(result1.group())

result2 = re.match('\D\D\D\d种口味', str1)
print(result2.group())
