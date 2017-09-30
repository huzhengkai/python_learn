import urllib
import urllib.request

data={}
data['word']='Jecvay Notes'
print(type(data))  #<class 'dict'>
url_values=urllib.parse.urlencode(data) #word=Jecvay+Notes
url="http://www.baidu.com/s?"
full_url=url+url_values  #http://www.baidu.com/s?word=Jecvay+Notes

data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)