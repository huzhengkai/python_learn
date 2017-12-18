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

