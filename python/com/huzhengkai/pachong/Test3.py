from nltk import word_tokenize
from nltk import Text
from nltk import pos_tag
from urllib.request import urlopen
from bs4 import BeautifulSoup

text = word_tokenize("The dust was thick so he had to dust")
print(text)
t = Text(text)
print(type(t))
print(t.tokens)
a = pos_tag(text)
print(a)

