"""函数：
def name (param1, param2...):
    statement
    ...
    return 返回值
"""
def get_sum(a, b):
    sum = a + b
    return sum

add = get_sum
result1 = get_sum(1, 2)
result2 = add(3, 4)
print(result1)
print(result2)
