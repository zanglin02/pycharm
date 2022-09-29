# 打印九九乘法表
i = 1
while i <= 9:
    j = 1  # j是列计数
    while j <= i:
        print(f'{j}*{i}={j*i}', end='\t')
        j += 1
    print('')  # 为了在每行结束的时候换行
    i += 1
