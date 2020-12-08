# 问题1： 子类中如何锚定一个父类的变量

# %% 

class School(object):
    """
    建一所学校
    """
    def __init__(self, school_name):
        self.school_name = school_name
        self.students_list = []
        self.teachers_list = []
        print('{}大学建立了'.format(self.school_name ))
    
    def hire(self, teacher_name):
        self.teachers_list.append(teacher_name)
        print('我们聘用了一个新老师{}'.format(teacher_name))

    def enroll(self, student_name):
        self.students_list.append(student_name)
        print('我们录用了一个新学员{}'.format(student_name))

class Grade(School):
    """
    建立一个专业
    """
    def __init__(self, grade_name, obj_school):
        # super(Grade, self).__init__(school_name)
        super().__init__(obj_school.school_name)
        # self.father = obj_school
        self.grade_name = grade_name
        self.grade_course = []
        print('专业{}建立了，他隶属于{}大学'.format(self.grade_name, self.school_name))

    def add_course(self, course_name):
        """
        给专业增加课程
        """
        self.grade_course.append(course_name)

class School_number(object):
    # 学校的人员
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list=[]
        
        print("我叫{}，我是一个{}".format(self.name, self.role))

class Student(School_number):
    """
    name, age, sex
    id, mark_list, course_list
    """
    id = {}

    def __init__(self, name, age, sex):
        super().__init__(name, age, sex, 'student')
        self.mark_list={}
        self.course_list = []
    
    def enroll(self, grade):
        if grade.grade_name not in self.id.keys():
            grade.enroll(self.name)
            grade_id = grade.school_name[0:2] +'-'+ grade.grade_name[0:2] + '-S-' + str(len(grade.students_list)).zfill(2)
            self.id = dict(self.id, **{grade.grade_name:grade_id})
            print('学员{}注册{}专业成功, 学号为{}'.format(self.name, grade.grade_name, self.id[grade.grade_name]))
        else:
            print('已有学号{},不需要重新注册'.format(self.id))

    def pay(self, grade, course):
        if course not in grade.grade_course:
            print('该专业无此项课程')
        elif course in self.course_list:
            print('您已报名{}, 请勿重新报名')
        else:    
            self.course_list.append(course)
            print('{}已报名{}课程, 您所有的课程为{}'.format(self.name, course, self.course_list))
    
    def praise(self,obj):
        print("{}觉得{}课真棒".format(self.name,obj.name))
            
    def mark_check(self):
        for i in self.mark_list.items():
            print(i)



abc = School('abc')

pyth = Grade('python', abc)
xiaomin = Student('小明', 14, 'F')
pyth.add_course('爬虫')
print('开始操作学生####')
xiaomin.enroll(pyth)
xiaomin.pay(pyth, '爬虫')

# %%
a = [1, 2, 3, 4]
b = [10, 9, 8]
c = a + b

print(c)

a = a + [5, 6]

print(c)
# %%
a = 'abc大学'

# %%
