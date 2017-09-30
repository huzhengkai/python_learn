import os,sys,configparser

os.chdir(sys.path[0]) #改变当前工作目录到该py所在的路径下
cp = configparser.ConfigParser(allow_no_value=True)
cp.read('baidu.conf',encoding='utf-8')

options=cp.options('baidu')  #['msj', 'mddc', 'mpos', 'fbfq', 'fbdk', 'tx', 'xykdb', 'fmxx', 'qt']
#print(options)
print("-------------------------------")
for option in options:
    o_keywords=cp.get('baidu',option)
    print(o_keywords)
    print("**************")
a = [1,'a',34,'sfa']
#for index,i_keyword in enumerate(a):
#    print(str(index)+"  "+str(i_keyword))
