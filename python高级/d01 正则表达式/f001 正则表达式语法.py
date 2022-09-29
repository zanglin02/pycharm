# python中使用re模块来做正则匹配
import re

# re.match(正则表达式， 需要匹配的字符串)
result = re.match('helllo', 'hello re!!!')
print(f"result's type:{type(result)}")
# 使用group()拿到匹配结果
info = result.group()
# 打印结果
print(f'info:{info}')