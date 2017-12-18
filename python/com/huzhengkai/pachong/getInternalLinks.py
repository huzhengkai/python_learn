from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

addressParts = splitAddress("http://oreilly.com")
print(addressParts)


def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

html = urlopen("http://oreilly.com")
bsObj = BeautifulSoup(html, "html.parser")

a = getInternalLinks(bsObj,urlparse("http://oreilly.com").netloc)
print(a)