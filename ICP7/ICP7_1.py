import requests
from bs4 import BeautifulSoup
import nltk
import string
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
#nltk.download()
import os
remove = dict.fromkeys(map(ord, '\n' + string.punctuation))
file = open('input.txt', 'a+', encoding='utf-8')
html=requests.get("https://en.wikipedia.org/wiki/Google")
bsObj = BeautifulSoup(html.content, "html.parser")
file.write(str(bsObj.text))

sentence = open("input.txt", encoding='utf-8').read().translate(remove)
stokens = nltk.sent_tokenize(sentence)
wtokens = nltk.word_tokenize(sentence)
for s in stokens:
    print(s)
for t in wtokens:
    print(t)

#POS
print(nltk.pos_tag(wtokens))

#STEMMING
print('--------Stemming---------')
pStemmer = PorterStemmer()
lStemmer = LancasterStemmer()
sStemmer = SnowballStemmer('english')
for i in wtokens:
    print(pStemmer.stem(i), lStemmer.stem(i), sStemmer.stem(i))

#LEMMATIZATION
print('--------lemmatization---------')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
for j in wtokens:
    print(lemmatizer.lemmatize(j))

#TRIGRAM

from nltk.util import ngrams
trigrams = list(ngrams(wtokens, 3))
print(trigrams)

#Named Entity Recognition

from nltk import wordpunct_tokenize, pos_tag, ne_chunk

print(ne_chunk(pos_tag(wordpunct_tokenize(s))))






