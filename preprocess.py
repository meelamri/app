# coding: utf-8
import preprocessor as p
import nltk
import string
from nltk.corpus import stopwords
from itertools import chain
from nltk.stem import *
from nltk.stem.porter import *
from nltk.stem.snowball import FrenchStemmer


def tokinizer(sentence):
	return  (nltk.word_tokenize(sentence))


def WordList_to_sentence(wordlist):
	sentence=""
	for word in wordlist:
		sentence =sentence+ " " + word
	return sentence



def stop (text):
	stop_words = stopwords.words('french')
	stop_words.append('les')
	stop_words.append('ceci')
	text =tokinizer(text)
	mynewtext = [w for w in text if w not in stop_words]
	return mynewtext

def punc (text):
	exclude = set(string.punctuation)
	text= ''.join(ch for ch in text if ch not in exclude)
	return text



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



def Find_Hashtag(sentence):
	finded=[]
	finded_=[]
	words = sentence.split()
	finded=[w for w in words if w[0] in '#']
	for word in finded:
		finded_.append(word[1:])
	return finded_

def remove_hashtag(sentence):
	stopwords=[]
	base = tokinizer(sentence)
	stopwords.append([w for w in base if w.startswith('#')])
	mynewtext = [w for w in base if w not in stopwords[0]]
	return WordList_to_sentence(mynewtext)

def append_n(sentence,word,n):
	mynewtext=[]
	for i in range (n):
		mynewtext.append(word)
		bloc=(WordList_to_sentence(mynewtext))
	return  " "+bloc


def hashtag_power(sentence):
	result=sentence
	finded=Find_Hashtag(sentence)
	for w in finded :
		tmp=append_n(sentence,w,10)
		result=result+tmp
	return result
		
def Enleve_Accents(txt):
    ch1 = u"àâçéèêëîïôùûüÿ"
    ch2 = u"aaceeeeiiouuuy"
    s = ""
    for c in txt:
        i = ch1.find(c)
        if i>=0:
            s += ch2[i]
        else:
            s += c
    return s
def set_sentence(sentence):
	p.set_options(p.OPT.URL, p.OPT.EMOJI)
	sentence=p.clean(sentence)
	sentence=hashtag_power(sentence)
	p.set_options(p.OPT.HASHTAG)
	sentence=p.clean(sentence)
	sentence=punc(sentence)
	sentence=sentence_stemmed(sentence)
	sentence=Enleve_Accents(sentence)
	return sentence

def set_sentence_(sentence):
	p.set_options(p.OPT.URL, p.OPT.EMOJI)
	sentence=p.clean(sentence)
	sentence=hashtag_power(sentence)
	p.set_options(p.OPT.HASHTAG)
	sentence=p.clean(sentence)
	sentence=punc(sentence)
	sentence=Enleve_Accents(sentence)
	return sentence

def set_corpus(corpus):
	corpus_=[]
	for sentence in corpus :
		corpus_.append(set_sentence_(sentence))
	return corpus_


if __name__ == '__main__':
	sentence="un test de suppression des mots non signifiant, ce test contient des liens et àâçéèêëîïôùûüÿ , des hashtag et des arobase 👍 https://google.fr @AROBASE #HASHTAG #ALORS #FINI"
	print "origin:"
	print sentence
	print "set:"
	print set_sentence(sentence)
