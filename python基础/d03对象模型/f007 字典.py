# 字典： 多个键值对 key value组成
# key 不可变类型
a = {1: 5, 'key1': 'value1'}
print(a['key1'])
a['key1'] = 100
print(a['key1'])
a['key2'] = 500
print(a)

# 清空字典 clear()
a.clear()
print(a)

# get(), pop()
a = {1: 5, 'key1': 'value1'}
b = a.get(1)
print(b)
c = a.get('key2', 0)
print(c)
# pop 删除并返回对应的键值对,如果没有这个key，则返回第二个参数
d = a.pop('key1')
print(d)
print(a)
e = a.pop('key2', 0)
print(e)
