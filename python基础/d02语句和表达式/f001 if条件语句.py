# if条件判断语句
Tom = 38.5
if Tom > 37.2:
    print('Tom 体温过高，不能进入车站')
else:
    print('Tom 体温正常， 请进')

# 多重判断：
age = int(input('请输入您的年龄'))
if age < 6:
    print(f'您的年龄为{age},不能接种疫苗')
elif (age >=6) and (age <= 60):
    print(f'您的年龄为{age},可以接种疫苗')
else:
    print(f'您的年龄为{age},不能接种疫苗')
