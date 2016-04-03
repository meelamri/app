# coding: utf-8
#corpus=['Rendez-vous au Boogie Spirit Festival ce weekend à Illkirch','Samedi 6 Février, à la ComedieFr pour voir "La Double inconstance" de Marivaux!','Toujours personne pour le 104paris ce soir ? Une pièce pleine d\'humour qui mêle théâtre et danse, ça ne vous dit pas ?','Pour les fans de réécritures de contes, ne manquez pas ‘The Forbidden Wish’ le 23 février prochain!']

import time
from tweepy_import import FilteredStream

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from get_categorie import get_categorie_
import nltk
from nltk.corpus import stopwords
import preprocessor as p
from preprocess import set_sentence
from user_categories import user_categories_

user_cat=user_categories_()
Nocat="Halloween"

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})

class MyFilteredStream(FilteredStream):
    def __init__(self):

        self.criterias = {
            "track": user_cat,
            "locations": [-0.6389644,44.8111222,-0.5334955,44.9163535],
            "lang": ["fr"]
        }
        FilteredStream.__init__(self, self.criterias, 10, "config.json")

    def action(self, tweets_list):
        corpus = []
        for t in tweets_list:
            tweet = t["text"]
            tweet = p.clean(tweet.encode("utf-8"))
            #tweet = set_sentence(tweet.encode("utf-8"))
           
            s=get_categorie_([tweet])
            if (s != Nocat):
                corpus.append(tweet)
                t["cat"]=s
                print tweet
                print t
        


        

       

stream = MyFilteredStream()
stream.stream()
