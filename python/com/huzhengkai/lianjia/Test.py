import math
import requests
from bs4 import BeautifulSoup



def getHTMLText(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    return response.text


house_urls = ["https://cd.lianjia.com/ershoufang/106100843735.html","https://cd.lianjia.com/ershoufang/106100805221.html","https://cd.lianjia.com/ershoufang/106100858149.html",
              "https://cd.lianjia.com/ershoufang/106100560654.html","https://cd.lianjia.com/ershoufang/106100503910.html","https://cd.lianjia.com/ershoufang/106100779271.html"]

file = open('lianjia.csv','w',encoding = 'utf-8')
for url in house_urls:
    res = getHTMLText(url)
    soup = BeautifulSoup(res, 'html.parser')
    xiaoqumingcheng = soup.find_all("a",attrs={"class":"info ","target":"_blank"})[0].get_text()
    base_info = soup.find_all("div",attrs={"class":"base"})[0].find_all("div",attrs={"class":"content"})[0].find_all("li")
    fangwuhuxing = base_info[0].get_text().replace("房屋户型","")
    louceng = base_info[1].get_text().replace("所在楼层","")
    mianji = base_info[2].get_text().replace("建筑面积","")
    chaoxiang = base_info[6].get_text().replace("房屋朝向","")
    quyu = soup.find_all("a",attrs={"href":"/ershoufang/jinjiang/","target":"_blank"})[0].get_text()
    price = soup.find_all("span",attrs={"class":"total"})[0].get_text()+"万"
    danjia = soup.find_all("span",attrs={"class":"unitPriceValue"})[0].get_text()
    jianzhushijian = soup.find_all("div",attrs={"class":"subInfo"})[2].get_text()[0:5]
    print(xiaoqumingcheng)
    print("______________________")

    # 将上面的各字段信息值写入并保存到csv文件中
    list1 = [xiaoqumingcheng,fangwuhuxing,mianji,quyu,louceng,chaoxiang,price,danjia,jianzhushijian]
    file.write(','.join('%s' %id for id in list1)+'\n')

# 关闭文件（否则数据不会写入到csv文件中）
file.close()
