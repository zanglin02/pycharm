name = 'Tom'
age = 18
weight = 75.5
student_id = 1

# 我的名字是Tom
print('我的名字是%s' % name)
print('我的名字是{}'.format(name))
"""
f字符串:  f'我的名字是{name}'
         大括号内放入想要替换字符串内的变量
"""
print(f'我的名字是{name}')

# 我的名字是Tom，我明年19岁
print(f'我的名字是{name},我明年{age+1}岁')

# 转义字符 \n换行 \t一个tab的间隔（4个空格）
print(f'我的名字是{name}\n我明年{age+1}岁')

print('--------分割线--------')
# print函数有一个参数 end 默认值为'\n'
print('hello', end=',')
print('world', end='!!!')
