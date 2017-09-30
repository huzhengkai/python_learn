import urllib.request

url = "http://www.baidu.com"
a = urllib.request.urlopen(url)
print(type(a))  #<class 'http.client.HTTPResponse'>
print(a.geturl())  #http://www.baidu.com
print(a.info())  #
print(a.getcode())  #200
data = a.read()
data = data.decode('UTF-8')
print(data)  #html