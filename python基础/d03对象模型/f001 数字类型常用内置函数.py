# abs() 返回对象的绝对值
a = -1
print(abs(a))

# max(), min(), sum()
# 返回最大值， 最小值， 求和计算
print(max(1, 2, 3, 6, 2, 65, 7, 32))
a = [1, 2, 37, 2, 1, 2462, 123, 2834]
print(sum(a))

import math
b = 144
math.sqrt(b)  # 返回b的平方根
math.pi  # 圆周率

import random  # 随即库
c = random.random()
print(c)
c = random.choice(a)
print(c)
c = random.randint(1, 10)  # 从1-10取随机整数
print(c)