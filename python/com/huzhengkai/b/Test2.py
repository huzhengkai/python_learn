import os,sys,configparser

os.chdir(sys.path[0]) #改变当前工作目录到该py所在的路径下

print("获取所有节点")
config = configparser.ConfigParser()
config.read('a.conf', encoding='utf-8')
ret1 = config.sections()
print(ret1)

print("获取指定节点下所有的键值对")
ret2 = config.items('section1')
print(ret2)

print("获取指定节点下所有的键")
ret3 = config.options('section1')
print(ret3)

print("获取指定节点下指定key的值")
v = config.get('section1', 'k1')
print(v)








