# %% 1.1 空'类'


class studert():
    # 如果类为空,则必须有`pass``
    pass


stu_xiaoming = studert()
del stu_xiaoming

print('***********************', '1.1', '***********************')
# %% 1.2 标准'类'


class student():

    name = None
    age = 18
    gender = 'man'
    course = 'Python'

    # 这个函数必须有(self)的变量传入
    def doHomeWork(self):
        print('我在做作业')
        return None


# 设置学生:'域名'
yu_min = student()
yu_min.name = '域名'

print('"域名"的信息:')
print(yu_min.name)
yu_min.doHomeWork()

print('***********************', '1.2', '***********************')
# %% 1.3 所有实例
print('student的所有实例为:')
student.__dict__

print('***********************', '1.3', '***********************')
# %% 1.4 self


class student():

    name = None
    age = 18
    gender = 'man'
    course = 'Python'

    # 这个函数必须有(self)的变量传入
    def doHomeWork(self):
        self.name = '1110k'
        print(self.name, end=' ')
        print('正在做作业')
        return None

    def doHomeWorkagain():
        print('正在做作业')
        print(__class__.name)
        print(__class__.age)
        return None


# stu_xiaoming = student()
# stu_xiaoming.doHomeWork()
student.doHomeWorkagain()
# print(stu_xiaoming.name)
print(student.name)
print('***********************', '1.4', '***********************')
