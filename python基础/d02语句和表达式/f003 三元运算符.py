# 三元运算符
# a if 条件 else b
# 整体返回值 条件成立 返回a
#          条件不成立 返回b
age = int(input('请输入年龄'))
# 下面两段代码是等价的
if age >= 18:
     result = '成年'
else:
     result = '未成年'
print(result)

result = '成年' if age >= 18 else '未成年'
print(result)
