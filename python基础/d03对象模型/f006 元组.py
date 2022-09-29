# 元组就是不可变的列表 （）
a = (52, 31, 366, 2)
print(a[3])

a = [1, 2]
b = (5,'strint', a)
print(b)
a.append(5)  # 和b[2].append(5)
print(b)
