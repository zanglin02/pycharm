# 不定个数个参数
def func(a, *args, **kwargs):
    print(a)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    print('-----------')
x = 1
y = [5, 7, 1]
z = {'key1': 1, 'key2': 2}
func(x, *y, **z)

func(1, 2, 3, 4, 5, key1=1, key2=2)
