# for 临时变量 in 序列

a = [1, 6, 8, 4, 9]

for i in a:
    if i == 6:
        continue
    elif i == 4:
        break
    print(i)

