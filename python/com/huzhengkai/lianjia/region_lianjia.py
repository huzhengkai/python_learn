from importlib import reload

import requests
from bs4 import BeautifulSoup
import time
import sys



def getHTMLText(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    return response.text

#成都的所有区名称
areas = ["jinjiang","qingyang","wuhou","gaoxin7","chenghua","jinniu","tianfuxinqu","gaoxinxi1","shuangliu","wenjiang"
    ,"pidou","longquanyi","xindou"]

#把数据存入文件后，读取文件，解析数据后存入文件中


file = open('region_urls/'+sys.argv[1],'r',encoding = 'utf-8')
out = open('region_urls/'+sys.argv[1]+'_data_1.csv','w',encoding = 'utf-8')
for each_line in file:
    #print(each_line)
    url = str(each_line).replace("\n","")
    res = getHTMLText(url)
    soup = BeautifulSoup(res, 'html.parser')
    #time.sleep(1)
    aa = soup.find_all("a",attrs={"class":"info ","target":"_blank"})
    if len(aa)!= 0 :
        xiaoqumingcheng = aa[0].get_text()
    else:
        xiaoqumingcheng =""
    try:
        base_info = soup.find_all("div",attrs={"class":"base"})[0].find_all("div",attrs={"class":"content"})[0].find_all("li")
    except IndexError  as e:
        print(url)
        fangwuhuxing = ""
        louceng = ""
        mianji = ""
        chaoxiang = ""
    try:
        fangwuhuxing = base_info[0].get_text().replace("房屋户型","")
    except IndexError  as e:
        print("fangwuhuxing error")
        print(base_info)
        fangwuhuxing = ""
    try:
        louceng = base_info[1].get_text().replace("所在楼层","")
    except IndexError  as e:
        print("louceng error")
        print(base_info)
        louceng = ""
    try:
        mianji = base_info[2].get_text().replace("建筑面积","")
    except IndexError as e:
        print("mianji error")
        print(base_info)
        mianji = ""
    try:
        chaoxiang = base_info[6].get_text().replace("房屋朝向","")
    except IndexError as e:
        print("chaoxiang error")
        print(base_info)
        chaoxiang = ""
    quyu = str(sys.argv[1])
    try:
        price = soup.find_all("span",attrs={"class":"total"})[0].get_text()+"万"
    except IndexError as e:
        print("price error")
        print(url)
        price = ""
    try:
        danjia = soup.find_all("span",attrs={"class":"unitPriceValue"})[0].get_text()
    except IndexError as e:
        print("danjia error")
        print(url)
        danjia = ""
    try:
        jianzhushijian = soup.find_all("div",attrs={"class":"subInfo"})[2].get_text()[0:5]
    except IndexError as e:
        print("danjia error")
        print(url)
        jianzhushijian = ""
    # print(xiaoqumingcheng+"---"+fangwuhuxing+"---"+mianji+"---"+quyu
    #   +"---"+louceng+"---"+chaoxiang+"---"+price+"---"+danjia+"---"+jianzhushijian)
    print("---------------------")
    # 将上面的各字段信息值写入并保存到csv文件中
    list1 = [xiaoqumingcheng,fangwuhuxing,mianji,quyu,louceng,chaoxiang,price,danjia,jianzhushijian]
    out.write(','.join('%s' %id for id in list1)+'\n')
file.close()
out.close()
