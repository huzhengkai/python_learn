from numpy import *

a = random.rand(4,3)
print(type(a))
print(a)
#mat()函数可以将数组转化为矩阵
randMat = mat(a)
print(type(randMat))

ab = randMat.shape
print(ab)

#取矩阵的逆
invRandMat = randMat.I
myEye = randMat * invRandMat
print(myEye)

e = eye(4)
print(e)

aa = e.shape[0]
print(aa)

print("-------------")

returnMat = array([[1,2,3],[4,5,6]])
for i in returnMat:
    print(i)
a = len(returnMat)
print(a)

print(returnMat)
#获取第一行
print(returnMat[0])
#获取第一行
print(returnMat[0,:])
#获取第一列
print(returnMat[:,0])

print("-----------")

print(returnMat.max(0))


