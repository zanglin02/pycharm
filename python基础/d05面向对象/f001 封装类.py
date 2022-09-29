# 类的定义封装：

class Car:
    # __init__方法是创建实例对象调用，一般用于实例属性初始化
    def __init__(self, owner, color, type_):
        self.owner = owner  # 实例属性的初始化
        self.color = color
        self.type = type_

    def move(self):
        print(f'{self.owner}的车在移动')

    def __str__(self):
        return f'{self.owner}的{self.color}的{self.type}'
    def paint(self,new_color):
        if new_color in ['黄色','红色','蓝色','黑色','白色']:
            self.color = new_color
        else:
            print(f'{self.owner}不喜欢{new_color}')

car1 = Car('Jerry', '红', '大卡车')
print(car1.color)
car1.move()
print(car1)

car1.color = '黑色'
print(car1)


car1.color = '白色'
print(car1)
