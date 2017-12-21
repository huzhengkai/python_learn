import math
import requests
from bs4 import BeautifulSoup
import time

def getHTMLText(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    return response.text

#每一个二手房对应的url
house_urls = []
#成都的所有区名称
areas = ["jinjiang","qingyang","wuhou","gaoxin7","chenghua","jinniu","tianfuxinqu","gaoxinxi1","shuangliu","wenjiang"
    ,"pidou","longquanyi","xindou"]

#当页数超过最大页数时，并不会报错，而是显示最后一页
#现在的问题是，如何获取最大页数
#先爬取https://cd.lianjia.com/ershoufang/jinjiang/，获取二手房的数量，除以30取整，就是最大页数
for i in areas:
    #根据区名称创建csv文件
    file = open(i,'w',encoding = 'utf-8')
    url = 'https://cd.lianjia.com/ershoufang/%s/' %i
    res = getHTMLText(url)
    print(url)
    soup = BeautifulSoup(res, 'html.parser')
    total_houses = soup.find_all("h2",attrs={"class":"total fl"})
    #总的房间数量转为int类型
    total_houses = int(total_houses[0].span.get_text())
    #总页数取整
    page_num = math.ceil(total_houses / 30)
    page_urls = []
    for x in range(page_num):
        #拿到了每个区一页的url，剩下的就是拿到该页中，每个二手房的链接
        page_url = url+"pg"+str(x+1)
        print(page_url)
        htmlText = getHTMLText(page_url)
        #time.sleep(1)
        soup1 = BeautifulSoup(htmlText, 'html.parser')
        a_urls = soup1.find_all("a",attrs={"class":"img "})
        for house_url in a_urls:
            house_urls.append(house_url.attrs["href"])
            file.write(str(house_url.attrs["href"])+'\n')
            print(house_url.attrs["href"])
    file.close()
    print("___________________________")

#把数据存入文件后，读取文件，解析数据后存入文件中

