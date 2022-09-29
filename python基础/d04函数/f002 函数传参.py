
def func(a, b, c):
    print(a)
    print(b)
    print(c)
x = 5
y = 'hello'
z = [1, 2, 3]

# 位置传参
func(x, y, z)
# 关键字传参
func(x, c=y, b=z)
# func(x, c=y, z) 注意： 位置参数在前，关键字参数在后。

# 带有默认值的参数，要放在参数列表的最后面
# 取值如果该参数函数调用时未拿到值则使用默认值
def func1(a, b, c=1):
    print(a)
    print(b)
    print(c)
func1(1, 2)