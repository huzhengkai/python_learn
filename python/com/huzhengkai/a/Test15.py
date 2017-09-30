class Student(object):
    name = 'Student'  #可以直接在class中定义属性，这种属性是类属性，归Student类所有
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
print(s.name)
del s.name  #del删除的是变量，而不是数据
print(s.name)
print(Student.name)