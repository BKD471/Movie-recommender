# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 07:33:02 2021

@author: User
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df2=pd.read_csv('../datasets/movie_metadata.csv')
df2.columns
df2.shape
 
df2['title_year']

df2['title_year'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Year of Release-->')
plt.ylabel('No of Movies-->')

data=df2.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]

data.isna().sum()

def replacenan(x):
    
    if x is np.nan:
        return 'unknown'
    return x
        
    
data['director_name']=data['director_name'].apply(lambda x:replacenan(x))
data['actor_1_name']=data['actor_1_name'].apply(lambda x:replacenan(x))    
data['actor_2_name']=data['actor_2_name'].apply(lambda x:replacenan(x))    
data['actor_3_name']=data['actor_3_name'].apply(lambda x:replacenan(x))   


data['genres']=data['genres'].str.replace('|',' ')
data['movie_title']=data['movie_title'].str.lower()

data['movie_title'][1]
data['movie_title']=data['movie_title'].apply(lambda x:x[:-1])

data['combo']=data['actor_1_name']+' '+data['actor_2_name']+' '+data['actor_3_name']+' '+data['director_name']+' '+data['genres']

data.to_csv('../datasets/data.csv',index=False)







 