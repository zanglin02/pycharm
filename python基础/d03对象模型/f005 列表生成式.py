# 列表生成式
a = [i for i in range(10)]
print(a)

a = []
for i in range(10):
    a.append(i)
print(a)

# 构建一个10个1-100的随机整型的列表
import random
a = [random.random(0, 100) for i in range(10)]