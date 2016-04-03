from data_gathering import data_gathrering_
from preprocess import set_sentence_
from get_categorie import get_categorie_
from pylab import *



def user_categories_():
	data_gathrering_()
	X_test=[]
	fd=open("data","r")
	lines=fd.readlines()
	for line in lines:
		line=set_sentence_(line)
		X_test.append(line)

	userscategories=[]
	userscategories=get_categorie_(X_test)
	print userscategories

	compte = {}.fromkeys(set(userscategories),0)
	for valeur in userscategories:
    	 compte[valeur] += 1

	del compte[max(compte, key=compte.get)]
	categories=[]
	values=[]

	for key, value in compte.iteritems():
		print key, value
		categories.append(key)
		values.append(value)

	print categories,values
	return categories
	#pie(values, labels=categories)
	#axis('equal')

	#show()


