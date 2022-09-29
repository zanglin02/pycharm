'''
输入： input('输入提示’）
       返回值是用户输入的内容 注意：返回值类型为str字符串
'''

# 计算用户输入2个值的和
a = input('请输入第一个数字')
b = input('请输入第二个数字')
# a,b为str 需要强制转换成int类型计算
a = int(a)
b = int(b)
print(a+b)

