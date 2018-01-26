from numpy import *

a = tile([0,0],5)
print(a)
b = tile([0,0],(1,1))
print(b)
c = tile([0,0],(2,1))
print(c)

d = arange(2)
print(type(d))
print(d**2)
print("*****************")
e = array([[0,1,2],[2,3,4]])
f = e.sum(axis=0) #按列相加
print(f)

f = e.sum() #默认把所有元素相加
print(f)

f = e.sum(axis=1)
print(f)  #按行相加

g = array([3, 1, 2])
h = g.argsort()
print(type(h))
print(h)

for i in range(3):
    print(i)

dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]
num = len(dataSet[0])
print(num)
for i in range(num):
    featList = [example[i] for example in dataSet]
    print(featList)
    uniqueVals = set(featList)
    print(uniqueVals)

a = ['yes','no','yes']
print(a.count('yes'))


a=1       # 对象 1 被 变量a引用，对象1的引用计数器为1
b=a       # 对象1 被变量b引用，对象1的引用计数器加1
c=a       #1对象1 被变量c引用，对象1的引用计数器加1
del a     #删除变量a，解除a对1的引用
del b     #删除变量b，解除b对1的引用
print(c)  #最终变量c仍然引用1

classList = [example[-1] for example in dataSet]
print(classList)



















































































