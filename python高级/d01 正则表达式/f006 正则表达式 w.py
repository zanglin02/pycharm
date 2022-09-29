# \w 匹配一个非特殊字符，包含 字母，数字，下划线，汉字
# \W 除了小w以外的所有
import re
str = '我有小米 & 苹果'
result1 = re.match('\w\w\w\w\W\W\W\w\w', str)
print(result1.group())