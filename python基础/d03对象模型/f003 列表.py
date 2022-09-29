# 列表 【】 可变类型，有序序列
example = [548, 14, 3481]

# 向列表内添加元素 append()
example.append(100)
print(example)
# 在列表指定位置添加元素 insert()
example.insert(1, 'briup')
print(example)
# 列表的扩展
example_str = 'hello'
example.extend(example_str)
print(example)
example_list = [5, 1, 2]
example.extend(example_list)
print(example)
example += example_list
print(example)
list