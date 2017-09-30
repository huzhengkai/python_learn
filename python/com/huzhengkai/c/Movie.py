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

class Movie(object):
    def __init__(self, time,category,title,downloadURL):
        self.time = time
        self.category = category
        self.title = title
        self.downloadURL = downloadURL
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
        movie = Movie(time,category,title,downloadURL)
        movieList.append(movie)




def main():
    data = getHTMLText("http://www.dlkoo.com/down/index.asp?page=2")
    getMovieList(data)
main()


# if __name__ == '__main__':
#     url = "http://www.dlkoo.com/down/index-.asp?page="
#     i = 1
#     while i:
#        url1=url+str(i)
#        print(url1)
#        i=i+1

