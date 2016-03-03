# coding: utf-8
import nltk
from itertools import chain
from nltk.stem import *
from nltk.stem.porter import *
from nltk.stem.snowball import FrenchStemmer



def tokinizer(sentence):
	return  (nltk.word_tokenize(sentence))


#base1=tokinizer(sentence)
#print base1 

def stemm(word):
	stemmer = FrenchStemmer()
	return stemmer.stem(word)

#stemmed1 = [stemm(s) for s in base1]
#print stemmed1


def WordList_to_sentence(wordlist):
	sentence=""
	for word in wordlist:
		sentence =sentence+ " " + word
	return sentence

#wordList = stemmed1	
#print WordList_to_sentence(wordList)

def sentence_stemmed(sentence):
	base=tokinizer(sentence)
	stemmed_=[stemm(s) for s in base]
	result=WordList_to_sentence(stemmed_)
	return result

def corpus_stemmed(corpus):
	corpus_stemmed=[]
	for sentence in corpus:
		corpus_stemmed.append(sentence_stemmed(sentence))
	return corpus_stemmed

if __name__ == '__main__':
    
	sentence1=" continu continua continuait continuant continuation continuer continuera continuerait continueront continuez continuite"
	print "origin:"
	print sentence1
	print "stemmed:"
	print sentence_stemmed(sentence1)

	sentence2=" contraindre contraint contrainte contraintes contraire contraires contraria"
	print "origin:"
	print sentence2
	print "stemmed:"
	print sentence_stemmed(sentence2)

	sentence3=" majestueuse majestueusement majestueux"
	print "origin:"
	print sentence3
	print "stemmed:"
	print sentence_stemmed(sentence3)

	sentence4=" continuel continuelle continuellement continuelles continuels"
	print "origin:"
	print sentence4
	print "stemmed:"
	print sentence_stemmed(sentence4)

