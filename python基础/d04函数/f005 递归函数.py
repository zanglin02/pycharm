# 计算1-100的和
# 循环：
def sum_cycle(n):
    result = 0
    i = 1
    while i in range(1, n):
        result += i
    return result

# 递归:
def sum_recu(n):
    if n > 0:
        return n + sum_cycle(n-1)
    else:
        return 0
