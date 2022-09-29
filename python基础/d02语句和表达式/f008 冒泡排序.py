# 冒泡排序
a = [1, 6, 2, 87, 36, 24, 945, 21]
print('排序前：',a)
for i in range(1,len(a)):
    # 大循环次数 为长度减一 确定len-1 个数字的位置后，第一个数字也被确定
    for j in range(1,len(a)-i+1):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
print('排序后', a)


