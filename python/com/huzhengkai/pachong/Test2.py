from nltk import ngrams
from nltk import word_tokenize
from nltk import Text
from nltk import FreqDist

tokens = word_tokenize("Here is some not very interesting text some is is ")
text = Text(tokens)
count = text.count("is")
print(count) #1
twogram = ngrams(text,2)
for a in twogram:
    print(a)

fdist = FreqDist(text) #可以将Text对象放到一个频率分布对象FreqDist中
a = fdist.most_common(5)
print(a)




