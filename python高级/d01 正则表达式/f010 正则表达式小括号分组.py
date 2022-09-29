# （）将括号内的字符作为一个分组
import re
# 匹配163，126，qq邮箱
# 4-20位数字/下划线/字母@163/126/qq.com
str1 = 'hello_world99@126.com'
result = re.match('[0-9a-zA-Z_]{4,20}@(163|126|qq)\.com', str1)
if result:
    print(result.group())
else:
    print('匹配失败')

# 分别匹配出‘qq：12345’中的qq和12345
str2 = 'qq:12345'
result = re.match('(qq):([1-9]\d{4,10})', str2)
if result:
    print(result.group())
    print(result.group(1))
    print(result.group(2))
else:
    print('匹配失败')

# \num 引用某个分组匹配到的字符串
str3 = '<span>5555</span'
result = re.match('<[a-z]+>.*<[/a-z]+>', str3)
print(result.group())
result = re.match('<([a-z]+)>.*</\\1>')
print(result.group())
# 引用的是对应分组匹配匹配匹配到的字符串！！不是将分组内的表达式拿过来用，下面例子会匹配不到
str4 = "<span>5555</html>"
result = re.match('<([a-z]+)>.*</\\1>', str4)
if result:
    print(result.group())
else:
    print('匹配失败')