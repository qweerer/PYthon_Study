# 空'类'
class studert():
    # 如果类为空,则必须有`pass``
    pass


stu_xiaoming = studert()


# 标准'类'
class student():

    name = None
    age = 18
    gender = 'man'
    course = 'Python'

    def doHomeWork():
        print('我在做作业')
        return None


yu_min = student()
yu_min.name = '域名'
print(yu_min.name)
yu_min.doHomeWork()
