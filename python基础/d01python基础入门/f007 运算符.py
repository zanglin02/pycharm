# 赋值运算符：
# 单个变量赋值：
num = 5  # python弱类型语言。
num = 5.5
num = 'hello,python'

# 多个变量同时赋值
name, age, grade = 'Tom', 18, 12
x = y = 3.14

# 比较运算符
# ==,!=, >, <, >=, <=
# 比较运算符式子他会返回一个bool类型的值 True False

# 逻辑运算符： and, or, not
print(True and True)

a, b, c = 0, 1, 2
print(a and b)  # 0
print(a or b)  # 1

print(a and b and c)  # 0
print(a or b or c)  # 1


# 复合赋值运算符（算术运算符连接赋值符）
a = 1
a = a + 1  # 下方两行代码是等价的
a += 1

a -= 1
a *= 1 
