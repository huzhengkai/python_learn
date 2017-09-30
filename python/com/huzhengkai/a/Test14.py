import sys
print(sys.path)


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 98)
print(bart._Student__name)

class Animal(object):
    def run(self):
        print('Animal is running...')
class Timer(object):
    def run(self):
        print('Start...')

a = len('ABC')
b = 'ABC'.__len__()
print(a == b)

class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))


class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
c = hasattr(obj, 'x') # 有属性'x'吗？
print(c)
d = hasattr(obj, 'y') # 有属性'y'吗？
print(d)
setattr(obj, 'y', 19) # 设置一个属性'y'
e =  hasattr(obj, 'y') # 有属性'y'吗？
print(e)
f =  getattr(obj, 'y') # 获取属性'y'
print(f)
g = obj.y
print(g)








