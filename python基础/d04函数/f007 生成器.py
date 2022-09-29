# 生成器的关键字： yield
def func():
    print('开始执行')
    for i in range(5):
        yield i
        print('执行结束')

num = func()
print(num)

num1 = num.__next__()
print(num1)
num2 = num.__next__()
print(num2)
num.__next__()
num.__next__()
num.__next__()
