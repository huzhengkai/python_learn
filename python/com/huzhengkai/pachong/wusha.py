import os

import requests
from bs4 import BeautifulSoup
import string,re

def getHTMLText(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    return response.text
def getAllFiles(path):
    if not os.path.exists(path):#判断path是否存在
        return -1
    allfiles = []
    for root,dirs,names in os.walk(path):
        for filename in names:
            allfiles.append(os.path.join(root,filename))#路径和文件名连接构成完整路径
    return allfiles

path = "C:\\Users\\Administrator\\Desktop\\xiaoshuo"
allfiles = getAllFiles(path)
for file in allfiles:
    if not "千" in file:
        os.remove(file)


# all= os.walk("C:\\Users\\Administrator\\Desktop\\xiaoshuo")
# print(type(all)) #<class 'generator'>
# for a in all:
#     print(a)

# text = getHTMLText("https://www.baidu.com/")


# print(string.punctuation)



