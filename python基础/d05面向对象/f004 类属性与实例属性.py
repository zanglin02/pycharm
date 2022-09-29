class Chinese:
    skinColor = '黄色'
    hairColor = '黑色'

    def __init__(self, name):
        self.name = name

    def change_hair_color(self, new_color):
        self.hairColor = new_color

    @classmethod  # 类方法 装饰器
    def change_hair_color_(cls, new_color):
        cls.hairColor = new_color

    @staticmethod  # 静态方法
    def display():
        print('这里是静态方法')
xiaoming = Chinese('小明')
print(Chinese.hairColor)
print(xiaoming.hairColor)

xiaoming.change_hair_color('金色')
print('小明染了金色头发')
print(Chinese.hairColor)
print(xiaoming.hairColor)


