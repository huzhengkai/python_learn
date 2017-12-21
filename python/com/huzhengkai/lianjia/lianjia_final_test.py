#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import requests
from bs4 import BeautifulSoup
import multiprocessing
from requests import HTTPError

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


def getErShouFang(area):
    a = os.path.getsize('region_urls/'+area)
    file = open('region_urls/'+area,'r',encoding = 'utf-8')
    out = open('data/'+area+'_data.csv','w',encoding = 'utf-8')
    for each_line in file:
        try:
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
                louceng = ""
                mianji = ""
                chaoxiang = ""
                fangwuhuxing = ""
                for info in base_info:
                    s = str(info.get_text())
                    if s.find("所在楼层")!= -1:
                        louceng = s.replace("所在楼层","")
                    elif s.find("建筑面积")!= -1:
                        mianji = s.replace("建筑面积","")
                    elif s.find("房屋朝向")!= -1:
                        chaoxiang = s.replace("房屋朝向","")
                    elif s.find("房屋户型")!= -1:
                        fangwuhuxing = s.replace("房屋户型","")
            except IndexError  as e:
                print("base_info error..."+url)
                fangwuhuxing = ""
                louceng = ""
                mianji = ""
                chaoxiang = ""
            quyu = str(area)
            try:
                price = soup.find_all("span",attrs={"class":"total"})[0].get_text()+"万"
            except IndexError as e:
                print("price  error..."+url)
                price = ""
            try:
                danjia = soup.find_all("span",attrs={"class":"unitPriceValue"})[0].get_text()
            except IndexError as e:
                print("danjia  error..."+url)
                danjia = ""
            try:
                jianzhushijian = str(soup.find_all("div",attrs={"class":"subInfo"})[2].get_text()[0:5])
                if jianzhushijian.find("/")!=-1:
                    jianzhushijian.replace("/","")
            except IndexError as e:
                print("jianzhushijian  error..."+url)
                jianzhushijian = ""
            # 将上面的各字段信息值写入并保存到csv文件中
            list1 = [xiaoqumingcheng,fangwuhuxing,mianji,quyu,louceng,chaoxiang,price,danjia,jianzhushijian]

            out.write(','.join('%s' %id for id in list1)+'\n')
            print("one house is collected...")
        except HTTPError:
            print("the house is sold..."+url)
    file.close()
    out.close()
if __name__ == '__main__':
    #创建5个进程的进程池
    pool = multiprocessing.Pool(processes = 5)
    for area in areas:
        pool.apply_async(getErShouFang,(area,))

    pool.close()
    pool.join()
    print("all done...")
