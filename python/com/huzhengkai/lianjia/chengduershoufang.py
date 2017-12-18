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
#先怕取https://cd.lianjia.com/ershoufang/jinjiang/，获取二手房的数量，除以30取整，就是最大页数
for i in areas:
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
        time.sleep(1)
        soup1 = BeautifulSoup(htmlText, 'html.parser')
        a_urls = soup1.find_all("a",attrs={"class":"img "})
        for house_url in a_urls:
           house_urls.append(house_url.attrs["href"])
           print(house_url.attrs["href"])

    print("___________________________")



print(len(house_urls))

file = open('lianjia.csv','w',encoding = 'utf-8')
for url in house_urls:
    res = getHTMLText(url)
    soup = BeautifulSoup(res, 'html.parser')
    time.sleep(1)
    aa = soup.find_all("a",attrs={"class":"info ","target":"_blank"})
    if len(aa)!= 0 :
        xiaoqumingcheng = aa[0].get_text()
    else:
        xiaoqumingcheng =""

    base_info = soup.find_all("div",attrs={"class":"base"})[0].find_all("div",attrs={"class":"content"})[0].find_all("li")
    try:
        fangwuhuxing = base_info[0].get_text().replace("房屋户型","")
    except IndexError  as e:
        print("fangwuhuxing发生了异常"+e)
        fangwuhuxing = ""

    try:
        louceng = base_info[1].get_text().replace("所在楼层","")
    except IndexError  as e:
        print("louceng发生了异常"+e)
        louceng = ""

    try:
        mianji = base_info[2].get_text().replace("建筑面积","")
    except IndexError as e:
        print("mianji发生了异常"+e)
        mianji = ""

    try:
        chaoxiang = base_info[6].get_text().replace("房屋朝向","")
    except IndexError as e:
        print("chaoxiang发生了异常"+e)
        chaoxiang = ""

    try:
        quyu = soup.find_all("a",attrs={"href":"/ershoufang/jinjiang/","target":"_blank"})[0].get_text()
    except IndexError as e:
        print("quyu发生了异常"+e)
        quyu = ""

    try:
        price = soup.find_all("span",attrs={"class":"total"})[0].get_text()+"万"
    except IndexError as e:
        print("price发生了异常"+e)
        price = ""

    try:
        danjia = soup.find_all("span",attrs={"class":"unitPriceValue"})[0].get_text()
    except IndexError as e:
        print("danjia发生了异常"+e)
        danjia = ""

    try:
        jianzhushijian = soup.find_all("div",attrs={"class":"subInfo"})[2].get_text()[0:5]
    except IndexError as e:
        print("danjia发生了异常"+e)
        jianzhushijian = ""



    print(xiaoqumingcheng+"---"+fangwuhuxing+"---"+mianji+"---"+quyu
          +"---"+louceng+"---"+chaoxiang+"---"+price+"---"+danjia+"---"+jianzhushijian)

    # 将上面的各字段信息值写入并保存到csv文件中
    list1 = [xiaoqumingcheng,fangwuhuxing,mianji,quyu,louceng,chaoxiang,price,danjia,jianzhushijian]
    file.write(','.join('%s' %id for id in list1)+'\n')

# 关闭文件（否则数据不会写入到csv文件中）
file.close()