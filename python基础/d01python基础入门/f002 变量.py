"""
命名规则：
1.不能使用系统关键字（橙色）和内建标识符（紫色）
2.不能使用数字开头
3.带有 _ 的标识符有特殊含义（详细见类）
4.一般命名方法：大驼峰，小驼峰，下划线连接
"""
import sys
import keyword
print(keyword.kwlist)  # 打印系统关键字


class MyClass:  # 类名一般使用大驼峰
    pass


myClass = 1  # 小驼峰


def my_class():  # 下划线连接
    pass


print(myClass)
myClass = myClass + 1
print(myClass)