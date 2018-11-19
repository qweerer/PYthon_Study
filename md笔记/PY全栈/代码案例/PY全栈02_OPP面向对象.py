# %%
# 空'类'


class studert():
    # 如果类为空,则必须有`pass``
    pass


stu_xiaoming = studert()
del stu_xiaoming
# %%
# 标准'类'


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
# 设置学生:'芦苇'

# %%
print('student的所有实例为:')
student.__dict__
