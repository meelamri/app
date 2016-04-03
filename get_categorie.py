# coding: utf-8
#!/usr/bin/python

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn import preprocessing
import numpy as np
import string
import re
from train_generate import train
from preprocess import set_sentence_

def get_categorie_(X_test):

	X_train,Y_train,target_names=train()

	X_train=np.array(X_train)
	Y_train=np.array(Y_train)
	y_train_text = [x[0] for x in Y_train]
	lb = preprocessing.LabelBinarizer()
	Y = lb.fit_transform(y_train_text)


	classifier = Pipeline([
    	('vectorizer', CountVectorizer()),
    	('tfidf', TfidfTransformer()),
    	('clf', OneVsRestClassifier(LinearSVC()))])

	classifier.fit(X_train, Y)
	predicted = classifier.predict(X_test)
	all_labels = lb.inverse_transform(predicted)

	for item, labels in zip(X_test, all_labels):
		print ' => %s' % (labels)
	return all_labels


if __name__ == '__main__':
	X_test=[]
	sentence= raw_input('Donnez moi une phrase et je vous donne la categorie:\n')
	X_test.append(sentence)
	
	get_categorie_(X_test)
