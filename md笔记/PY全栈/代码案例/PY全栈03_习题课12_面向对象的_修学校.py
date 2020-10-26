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
    def __init__(self, grade_name, grade_number, obj_school, ):
        # super(Grade, self).__init__(school_name)
        super().__init__(obj_school.school_name)
        # self.father = obj_school
        self.grade_name = grade_name
        self.grade_number = grade_number
        self.grade_course = []
        print('专业{}建立了，他隶属于{}大学'.format(self.grade_name, self.school_name))

    def add_course(self, course_name):
        """
        给专业增加课程
        """
        self.grade_course.append(course_name)
    
    def

abc = School('abc大学')

avc = Grade('avc专业')
# %%
a = [1, 2, 3, 4]
b = [10, 9, 8]
c = a + b

print(c)

a = a + [5, 6]

print(c)

