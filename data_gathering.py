# coding: utf-8
#!/usr/bin/python


#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays a user's current timeline.
#-----------------------------------------------------------------------
import sys 
from twitter import *
import sys, os
from preprocess import set_corpus
from preprocess import set_sentence_
import nltk
import string
from nltk.corpus import stopwords
from itertools import chain
from nltk.stem import *
from nltk.stem.porter import *
from nltk.stem.snowball import FrenchStemmer



def data_gathrering_():
#-----------------------------------------------------------------------
# load the file config.py containing the configurations infos 
#-----------------------------------------------------------------------
	config = {}
	execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object using the config file 
#-----------------------------------------------------------------------
	twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

#-----------------------------------------------------------------------
# retrieve the user using the command line
#-----------------------------------------------------------------------

	user = sys.argv[1] 

#-----------------------------------------------------------------------
# query into the user timeline. The first query is used to retrieve 
# the user tweets's timeline, the second is´to retrieve a user's 
# favorite list of tweets and the third is used to retrieve timeline
# tweets of the user using the infos of the config file
#-----------------------------------------------------------------------
	results0 = twitter.statuses.user_timeline(screen_name = user, count=3200)
	results1=(twitter.favorites.list(screen_name = user, count=3200))
	results2 = twitter.statuses.home_timeline(count = 50)

#-----------------------------------------------------------------------
# loop through each status item, and extract the text content 
#-----------------------------------------------------------------------

	corpus=[]
	corpus_=[]
	i = 0

	for status in results0:
		i+=1
		#print " %s" % ( status["text"])
		corpus=status["text"]+'\n'
		s = status["text"].encode("utf-8")
		print s 
		corpus_=set_sentence_(s)
	

	for status in results1:
	#print " %s" % ( status["text"])
		corpus+=(status["text"])+'\n'
		s = status["text"].encode("utf-8")
		corpus_=set_sentence_(s)

	for status in results2:
		#print " %s" % ( status["text"])
		corpus+=(status["text"])+'\n'
		s = status["text"].encode("utf-8")
		corpus_=set_sentence_(s)

#print corpus


	



#-----------------------------------------------------------------------
# exort our corpus into the file data 
#-----------------------------------------------------------------------

	filepath = "data"
	with open(filepath, 'w') as f:
		f.write(corpus.encode("utf-8"))
		print(" tweets successfully exported to " + filepath)
	return corpus_


