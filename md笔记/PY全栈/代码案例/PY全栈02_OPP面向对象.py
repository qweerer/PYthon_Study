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
# %% 1.5 mro


class Animos():

    def gogo(self):
        print('animos!go!')


class Puru(Animos):
    pass


class cat(Puru):

    def gogo(self):
        print('Cat!go!')
        super().gogo()


haha = cat()
haha.gogo()
# print('&'*20)
# Animos.gogo(haha)
print('&'*20)
print(Puru.__mro__)
print(cat.__mro__)
print('***********************', '1.5', '***********************')
# %% 1.6 继承自己的想法


class A():
    def __init__(self):
        print('我是A')


class B1(A):
    def __init__(self):
        print('我是B1,下面是我爸的发言')
        super.__init__(A)


class B2(A):
    def __init__(self):
        print('我是B2')

    def work(self):
        print('干活中')


class C(B1):
    def __init__(self):
        print('我是C')

    def work(self):
        b2 = B2()
        B2.work(b2)


abc = C()
abc.work()
print('***********************', '1.6', '***********************')

# %%标准写法
class Student(object):
    def __init__(self, name, age, scores):
        """
        定义一个学生，self为其本身，其他3个是其属性
        """
        self.name = name
        self.age = age
        self.scores = scores

a = Student('小明', 12, [12,13,120])
print(a.age)


# %%
class student(object):
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores
'''        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_course(self):
        return max(self.scores)
'''    

zz = student("周周", 18, [80,100,90])
#print(zz.get_name())
#print(zz.get_age())
#print(zz.get_course())

# %%
