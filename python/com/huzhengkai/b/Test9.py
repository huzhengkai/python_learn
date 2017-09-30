import logging,os,json
import requests,urllib,configparser,sys,multiprocessing,threading
from bs4 import BeautifulSoup
from datetime import datetime


def download(url):
    try:
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                   'Host': 'www.baidu.com'
                   }
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        else:
            logging.error(u'请求失败:%s %s'%(response.url,response.status_code))
            return None
    except Exception as e:
        logging.error(u'发生未知错误')
        return None

wd = {'wd':'18512805771贷款无烦恼'}
a = urllib.parse.urlencode(wd)
#print(a) #wd=18512805771%E8%B4%B7%E6%AC%BE%E6%97%A0%E7%83%A6%E6%81%BC
url = "https://www.baidu.com/s?wd=18512805771%E8%B4%B7%E6%AC%BE%E6%97%A0%E7%83%A6%E6%81%BC&pn=0&cl=3&rn=10"
html=download(url)
#print(html)

soup = BeautifulSoup(html, 'lxml')
b = soup.find_all('div',class_='c-border')
print(b)