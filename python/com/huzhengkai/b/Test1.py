import re
import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  #响应码如果不是200，则会抛出异常
        r.encoding = r.apparent_encoding  #使用apparent_encoding可以获得网站编码，然后再赋值编码，这样就不会有乱码的问题了
        return r.text
    except:
        return ""
a = getHTMLText("http://quote.eastmoney.com/stocklist.html")

soup = BeautifulSoup(a,"html.parser")
b = soup.find_all("a") #b是一个list
#print(b)
lst = []
for i in b:
    try:
        href = i.attrs['href']
        c = re.findall(r"[s][hz]\d{6}", href)
        if(c.__len__()!=0): #由于有的元素内，不匹配正则表达式，所以为[]
            lst.append(c[0])
            #print(c)
    except :
        continue
#print(lst)


count = 0
for stock in lst:
    url = 'https://gupiao.baidu.com/stock/' + stock + ".html"
    html = getHTMLText(url)
    try:
        if html=="":
            continue
        infoDict = {}
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        stockInfo = soup.find('div',attrs={'class':'stock-bets'})

        name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
        infoDict.update({'股票名称': name.text.split()[0]})

        keyList = stockInfo.find_all('dt')
        valueList = stockInfo.find_all('dd')
        for i in range(len(keyList)):
            key = keyList[i].text
            val = valueList[i].text
            infoDict[key] = val

        #with open('D:/BaiduStockInfo.txt', 'a', encoding='utf-8') as f:
         #   f.write( str(infoDict) + '\n' )
        #    count = count + 1
         #   print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
    except:
       # count = count + 1
        #print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
        continue
