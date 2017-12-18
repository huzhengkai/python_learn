import requests
from bs4 import BeautifulSoup
import json

def getHTMLText(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    # response = requests.get(url, headers=headers,verify="E:/srca.cer")
    # response = requests.get(url, headers=headers,cert="E:/srca.cer")
    response = requests.get(url, headers=headers,verify=False)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    return response.text

text = getHTMLText("https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-18&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=CQW&purpose_codes=ADULT")
print(text)
dict = json.loads(text)
#result是一个list
result = dict['data']['result']
print(result)
#list中数据的格式：|预订|76000D22440B|D2244|ICW|FZS|ICW|CUW|06:44|09:02|02:18|N|y6iYkg1AVgyLdbioijyYMahg3fvTqYutBTZ8UK94HY9%2BkZxv|20171118|3|W1|01|04|0|0|||||||无||||无|无|||O0M0O0|OMO
#数据都是以|分隔的，我们打印一下每个每小段数据都是什么
c = 0
for i in result:
    for n in i.split('|'):
        print("[%s] %s"%(c,n))
        c = c+1
    c = 0
    break
#从上面的输出可以看到