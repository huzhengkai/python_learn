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
    print(url1)
    i=i+1