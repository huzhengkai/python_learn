import string
import operator

# class Test(object):
#     def __init__(self,test,time=""):
#         self.test = test
#
# test = Test("abc")
# print(test.time)



url = "http://www.dlkoo.com/down/index.asp?code=1&page="
i = 1
while i:
    if i ==3:
        break
    url1=url+str(i)
    #print(url1)
    i=i+1


set1 = {"a",1}
# print(set1.discard("a"))
set2 =set()
for s in set1:
    if s == 1:
        set2.add(s)
# print(set2)

# print(set1.difference(set2))

s = "554sjfslksdf"
input = bytes(s, "UTF-8")
print(input)

s2 = '涔辩爜'
print(s2.encode('gbk').decode("utf8"))

print(string.punctuation)

a = [1,2,3]
b = operator.itemgetter(1) #定义函数b，获取对象的第一个域的值
print(b(a)) #2
b = operator.itemgetter(1,0)#定义函数b，获取对象的第1个域和第0个域的值
print(b(a)) #(2, 1)

print("*****************")


L = [{1:5,3:4},{1:3,6:3},{1:1,2:4,5:6},{1:9}]
def f(x):
    return len(x)
a = sorted(L,key=f)
print(a) #[{1: 9}, {1: 5, 3: 4}, {1: 3, 6: 3}, {1: 1, 2: 4, 5: 6}]

print("*****************")

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
s = sorted(students, key=lambda student : student[2])
print(s) #[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

s1 = sorted(students, key=operator.itemgetter(2))
print(s1) #[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]