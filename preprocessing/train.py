# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:31:24 2021

@author: User
"""

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score,accuracy_score
import pickle


nltk.download('stopwords')


data=pd.read_csv('../datasets/reviews.txt',sep='\t',names=['Reviews','Comments'])

stopset=set(stopwords.words('english'))

vectorizer = TfidfVectorizer(use_idf = True,lowercase = True, strip_accents='ascii',stop_words=stopset)

X = vectorizer.fit_transform(data.Comments)
y = data.Reviews
filename='transform.pkl'
pickle.dump(vectorizer, open(filename, 'wb'))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# first lets train with train data only 
clf = naive_bayes.MultinomialNB()
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)
acc=accuracy_score(y_test,y_pred)*100
# accuracy is around 97.47%

# now train with entire data
clf = naive_bayes.MultinomialNB()
clf.fit(X,y)

y_pred=clf.predict(X_test)
acc=accuracy_score(y_test,y_pred)*100
# now accuracy is 98.77%

filename='nlp_model.pkl'
pickle.dump(clf,open(filename,'wb'))




