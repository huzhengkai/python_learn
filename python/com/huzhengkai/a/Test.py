import os
'''classmates = ['Michael', 'Bob', 'Tracy']
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for ch in 'ABC':
    print(ch)
def aaa():
    print('11111')
aaa()'''
print(os.getcwd())
#改变当前工作目录到指定的路径，必须是目录，不可以是文件
os.chdir('F:\\HeadFirstPython\\chapter3')
print(os.getcwd())
data = open('sketch.txt',encoding='utf-8')
print(data)
for each_line in data:
    #判断这行数据是否有:
    if not each_line.find(':')==-1:
        #返回一个tuple,1代表最多分成两个部分
        (role,line_spoken) = each_line.split(':',1)
        print(role,end='')
        print(' said: ',end='')
        print(line_spoken,end='')
data.close()


