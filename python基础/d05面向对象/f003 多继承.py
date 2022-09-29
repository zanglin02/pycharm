# 类的继承
# 1.专家  基类
class Expert:
    def __init__(self):
        self.technology = '治病的技术'

    def treatment(self):
        # 治病救人
        print(f'运用{self.technology}救治病人')


class School:
    name = 'xxxx学校'
    def __init__(self):
        self.technology_ = '基于教材的医术'

    def treatment(self):
        print(f'运用{self.technology_}救治病人')





# 2.学生 子类
class Student(School,Expert):  # 如果有同名的属性就打印第一个的属性
    # 继承自专家
    pass

# 3.创建子类对象
Tom = Student()
# 4.使用实例调用实例属性
print(Tom.technology_)
# 5.实例去调用实例方法：
Tom.treatment()


print(School.name)
print(Tom.name)
