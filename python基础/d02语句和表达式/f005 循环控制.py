# break : 跳出所属循环
# continue : 跳出当前次循环
i = 1
while i <= 5:
    if i == 4:
        print(f'吃了{i-1}个苹果，吃饱了')
        break
    print(f'正在吃第{i}个苹果')
    i += 1
print('结束')

print('------------分割------------')
i = 1  # 第几个苹果
count = 0  # 吃了几个苹果
while i <= 5:
    if count == 3:
        print('吃饱了')
        break
    if i == 3:
        print(f'第3个苹果坏了，不能吃')
        i += 1
        continue
    print(f'正在吃第{i}个苹果')
    i += 1
    count += 1
print('结束')


