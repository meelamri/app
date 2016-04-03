# coding: utf-8
#!/usr/bin/python


import sys 
import numpy as np
import os
import re
import string
from preprocess import Enleve_Accents

def train():
	X_train = []
	Y_train = []
	Target_name = []
	
	for element in os.listdir('dico'):
		X=[]
		if element.endswith('.txt') & os.path.exists("dico/"+element):
		   descriptor = element[:-4]
		   Target_name.append(descriptor)
		   fd=open("dico/"+element)
		   lines= fd.readlines()
		   for line in lines:
				wordList = line.split(" ")

				for w in wordList:
					
					X.append(w)
           	for w in X:
				Y_train.append([descriptor])

		X_train+=X

	return X_train, Y_train , Target_name	   



