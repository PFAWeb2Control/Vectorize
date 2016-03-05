# coding: utf-8
import nltk
from nltk.corpus import stopwords
import string
import WordAnalyse

def tokinizer(sentence):
	return  (nltk.word_tokenize(sentence))


def WordList_to_sentence(wordlist):
	sentence=""
	for word in wordlist:
		sentence =sentence+ " " + word
	return sentence


def http (text):
	stopwords=[]
	stopwords.append([w for w in text if 'https' and 'http' in w ])
	mynewtext = [w for w in text if w not in stopwords[0]]
	return mynewtext

def stop (text):
	stop_words = stopwords.words('french')
	stop_words.append('les')
	stop_words.append('ceci')
	text =tokinizer(text)
	mynewtext = [w for w in text if w not in stop_words]
	return mynewtext

def punc (text):
	text = text.translate(None, string.punctuation)
	return text 

def remove (text):
	text=punc(text)
	base=tokinizer(text)
	ttp=http(base)
	sentence=WordList_to_sentence(ttp)
	stop_words=stop(sentence)
	sentence=(WordList_to_sentence(stop_words))
	return sentence


	

if __name__ == '__main__':
	sentence=" ceci est un test de suppression, je garde que les mot signifiant, https://google.com "
	print "origin:"
	print sentence 
	print remove (sentence)
