import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook



wb = Workbook()
dest_filename = '大连生活网资源列表.xlsx'
#获取工作表
ws1 = wb.active
ws1.title = "资源"
def getHTMLText(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    return response.text

class Movie(object):
    def __init__(self, time,category,title,downloadURL,information):
        self.time = time
        self.category = category
        self.title = title
        self.downloadURL = downloadURL
        self.information = information
    def set(self, information):
        self.information = information
def getMovieList(htmlText):
    soup = BeautifulSoup(htmlText, 'html.parser')
    a = soup.select("li.tr")
    url = "http://www.dlkoo.com"
    movieList=[]
    for i in a:
        time = i.find_all("span",attrs={"class":"addt"})[0].text
        category = i.find_all("a",attrs={"class":"lei"})[0].text
        title = i.find_all("a",attrs={"class":"title"})[0].text
        downloadURL = url + i.find_all("a",attrs={"class":"title"})[0].attrs["href"]
        movie = Movie(time,category,title,downloadURL,"")
        if category!="动漫" and category!="游戏":
            movieList.append(movie)

    return movieList
def addInformationToMovie(movieList):
    for movie in movieList:
        downloadHTMLText = getHTMLText(movie.downloadURL)
        soup = BeautifulSoup(downloadHTMLText, 'html.parser')
        lists = soup.select("#contenthtml")
        if len(lists)!=0:
            information = lists[0]
            # print(information)
            # print("*******************************")
            movie.set(information.get_text())
            # print(movie.time+"---"+movie.category+"---"+str(movie.information))
    return movieList
#一行代表一个资源
def movieListSaveToCSV(movieInformationList):
    for movie in movieInformationList:
        row = []
        row.append(movie.time)
        row.append(movie.category)
        row.append(movie.title)
        row.append(movie.downloadURL)
        row.append(movie.information)
        ws1.append(row)
    wb.save(filename=dest_filename)

#n代表我们想要遍历的页数,n为10，遍历1-9页。
def generateURL(n):
    urlList=[]
    url = "http://www.dlkoo.com/down/index.asp?code=1&page="
    i = 1
    while i:
        if i ==n:
            break
        url1=url+str(i)
        urlList.append(url1)
        i=i+1
    return urlList

def main():
    urlList = generateURL(3)
    allMovie = []
    for url in urlList:
        data = getHTMLText(url)
        movieList = getMovieList(data)
        movieInformationList= addInformationToMovie(movieList)
        allMovie.extend(movieInformationList)

    movieListSaveToCSV(allMovie)

    # for movie in movieInformationList:
    #     # print(type(movie.time)+"---"+type(movie.category)+"---"+type(movie.title)+"---"+type(movie.downloadURL)+"---"+type(movie.information)) 这里会报错：TypeError: unsupported operand type(s) for +: 'type' and 'str'
    #     print(type(movie.time))
    #     print(type(movie.category))
    #     print(type(movie.title))
    #     print(type(movie.downloadURL))
    #     print(type(movie.information))
    #     print("***************************")


main()


# if __name__ == '__main__':
#     url = "http://www.dlkoo.com/down/index-.asp?page="
#     i = 1
#     while i:
#        url1=url+str(i)
#        print(url1)
#        i=i+1

