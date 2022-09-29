# 转义字符
# \+? 表示转义字符
# \n 换行 \t 一个tab=4个空格 \a 响铃 \\表示的是一个\

print('\a')
print('\\')
print(r'\\\n\t\s9')  # r开头的字符串 表示取消转义

print('--------分隔符(单独索引）--------')
example = 'Hello, World!'
print(example[5])  # 用下标取值
print(example[-1])
print('--------分隔符(2个索引）--------')
print(example[0:5])  # 左闭右开 打印索引0-4的内容
print(example[:5])
print(example[5:])
print(example[-5:-1])
print(example[-5:])
print('--------分隔符(2个索引+步长）--------')
print(example[:5:2])  # 2是步长
print(example[5:0:-1])  # 步长取负 索引按照原字符串顺序拿 之后再镜面翻转
print(example[:-6:-1])




print(len(example))  # 获取字符串长度

# 分割字符串 split()
str_list = example.split(',')
print(str_list)
str_list = example.split('l')  # 相邻的分隔符 会产生一个空字符串
print(str_list)

# 字符串替换
replaced_str = example.replace('l', '?')
print(replaced_str)
replaced_str = replaced_str.replace('?', 'l', 2)
print(replaced_str)

# 字符串插入 join()
example = ['b', 'r', 'i', 'u', 'p']
result = '_'.join(example)
print(result)
result = ''.join(example)
print(result)
