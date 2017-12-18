from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" or "www" that do
    #not contain the current URL
    for link in bsObj.findAll("a", href=re.compile(
                            "^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


html = urlopen("http://oreilly.com")
bsObj = BeautifulSoup(html, "html.parser")

list = getExternalLinks(bsObj,urlparse("http://oreilly.com").netloc)
print(list)

def getExternalLinks1(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    excludeUrl = urlparse(url).netloc
    externalLinks = []
    #Finds all links that start with "http" or "www" that do
    #not contain the current URL
    for link in bsObj.findAll("a", href=re.compile(
                            "^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

print(getExternalLinks1("http://oreilly.com"))
