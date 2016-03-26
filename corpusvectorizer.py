# coding: utf-8
import sys 
import numpy as np
from preprocess import set_sentence
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords

########################################################
#     intput_: corpus.txt                              #
#                                                      #
#     example: python corpusvectorizer.py corpus.txt   #
########################################################
corpus=[]
input_ = sys.argv[1]
fs=open(input_,'r')

lines = fs.readlines()
for line in lines:
	line =set_sentence(line)
	corpus.append(line)

	
stwf=stopwords.words('french')
stwf.append('les')
stwf.append('rt')


vectorizer=CountVectorizer(stop_words=stwf,decode_error ="ignore")
X = vectorizer.fit_transform(corpus)
X = X.toarray()

print X 