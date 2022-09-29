import re
# * 匹配前一个字符出现0-无限次 可有可无
result = re.match('[A-Za-z]*', 'M')
print(result.group())

result = re.match('[A-Za-z]*', 'hello python!')
print(result.group())

# + 匹配前一个字符一次或无数次
result = re.match('[A-Za-z]+', 'hello python!')
print(result.group())

result = re.match('co+l!', 'cooooooooool!!!')
print(result.group())

# ? 匹配前一个字符1次或0次
result = re.match('https?', 'http')
if result:
    print(result.group())
else:
    print('匹配失败')

# {m} 前一个字符出现m次
# {m,n} 匹配前一个字符出现m到n次
# 匹配一个6位密码: 不能用下划线开头 可以包含 字母 数字 下划线
# a = '_'
# result = re.match('[a-zA-z0-9]', a)
# print(result.group())
while True:
    input_ = input('请输入需要验证的密码: ')
    result = re.match('[a-zA-z0-9][0-9A-Za-z]{5}', input_)
    if result:
        print(result.group())
        print(f'可以使用，输入的密码为：{input_}')
    else:
        print('不符合密码规定')
