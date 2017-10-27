import requests,os
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

def downloadEveryNovel(downloadUrl,title):
    title = re.sub("\*+","",title)
    htmlText = getHTMLText(downloadUrl)
    soup = BeautifulSoup(htmlText, 'html.parser')
    novel = soup.find("div",attrs={"class":"yd_text2"})
    os.chdir("C:\\Users\\Administrator\\Desktop\\xiaoshuo")
    file = open(title,'w',encoding='utf-8')
    print(novel.get_text(),file=file)
    file.close()

baseUrl = "http://www.88dushu.com/xiaoshuo/42/42372/"
htmlText = getHTMLText(baseUrl)
soup = BeautifulSoup(htmlText, 'html.parser')
mulu = soup.find("div",attrs={"class":"mulu"})
li = mulu.find_all("li")
newli = []
for l in li:
    # print(type(l.get_text()))
    a = l.find_all("a")
    #去除没有链接，和其他内容的章节。。。
    if(len(a)!=0 and "章" in l.get_text()):
        newli.append(l)
for l in newli:
    title = l.get_text()
    downloadUrl = baseUrl + l.a.attrs['href']
    try:
        downloadEveryNovel(downloadUrl,title)
    except Exception as e:
        print(e)
    # print(title+"...."+downloadUrl)