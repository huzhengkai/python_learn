from types import MethodType
class Student(object):
    pass
s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果

#但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(25)

def set_score(self, score):
    self.score = score
Student.set_score = set_score

s.set_score(10)
s2.set_score(20)
print(s.score)
print(s2.score)
