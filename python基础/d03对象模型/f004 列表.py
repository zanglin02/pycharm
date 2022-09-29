example = [15, 164, 484, 1]
# 从列表移除某个元素 remove （匹配项
a = example.remove(484)
print(example)

# 从列表移除指定索引的元素 pop
b = example.pop(2)  # 返回列表对应下表的那个值
print(b)
print(example)



# 修改列表内容： 直接通过下标修改
example[0] = 100
print(example)
example[0], example[1] = example[1], example[0]
print(example)
print('----分隔符----')
# 排序 sort
example = [56, 222, 845, 1, 28]
example.sort()
print(example)
example.sort(reverse=True)
print(example)

# 列表倒置 reverse()
example.reverse()
print(example)