from numpy import *
num=0
while(num<5):
    random.seed(5)
    print(random.random())
    num+=1

print("***********")

num=0
random.seed(5)
while(num<5):
    print(random.random())
    num+=1