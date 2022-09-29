import random
# 匿名函数 lambda
a = lambda x: x+1

def func(x):
    return x+1

result = a(5)
# print(result)

# 使用场景 sorted函数内
a = [(random.randint(0, 100), i) for i in range(10)]
print(a)
b = sorted(a, key=lambda x: x[1], reverse=True)
# key 接受一个函数 参数为需要排序的对象整体，返回值是排序依据
print(b)
