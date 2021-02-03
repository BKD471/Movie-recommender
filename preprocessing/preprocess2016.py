# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:23:13 2021
142,144
@author: User
"""

import pandas as pd
import numpy as np

#extracting movies of 2016 from wikipedia
link_2016='https://en.wikipedia.org/wiki/List_of_American_films_of_2016'
df1=pd.read_html(link_2016,header=0)[3]
df2=pd.read_html(link_2016,header=0)[4]
df3=pd.read_html(link_2016,header=0)[5]
df4=pd.read_html(link_2016,header=0)[6]

df=df1.append(df2.append(df3.append(df4,ignore_index=True),ignore_index=True),ignore_index=True)

from tmdbv3api import TMDb
import json
import requests
tmdb=TMDb()
tmdb.api_key='2c4a17a043d93c60bd7f3fd7b0c00958'

from tmdbv3api import Movie
tmdb_movie=Movie()
def get_genre(x):
    genre=[]
    result=tmdb_movie.search(x)
    movie_id=result[0].id
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
    data_json=response.json()
    if data_json['genres']:
        n=len(data_json['genres'])
        for i in range(n):
            genre.append(data_json['genres'][i]['name'])
        return ' '.join(genre)
    else:
        return np.nan


df['genres']=df['Title'].apply(lambda x:get_genre(str(x)))

df_2016=df.loc[:,['Title','Cast and crew','genres']]
df_2016=df_2016.rename(columns={'Title':'movie_title'})
df_2016['Cast and crew'].dtype

def get_director(x):
    if " (director)" in x:
        return x.split('(director)')[0]
    elif " (director/screenplay)" in x:
        return x.split('(director/screenplay)')[0]
    elif " (directors/screenplay)" in x:
        return x.split('(directors/screenplay)')[0]
    elif " (director/story)" in x:
        return x.split('(director/story)')[0]
    elif " (director/writer)" in x:
        return x.split('(director/writer)')[0]
    elif " (directors)" in x:
        return x.split('(directors)')[0]
    
    
df_2016['director_name']=df_2016['Cast and crew'].apply(lambda x:get_director(str(x)))

def actor1(x):
    if " (screenplay)" in x:
        return (x.split(' (screenplay);')[-1]).split(', ')[0]
    elif " (director)" in x:
        return (x.split(' (director);')[-1]).split(', ')[0]
    elif " (director/screenplay)" in x:
        return (x.split(' (director/screenplay);')[-1]).split(', ')[0]
    elif " (directors/screenplay)" in x:
        return (x.split(' (directors/screenplay);')[-1]).split(', ')[0]
    elif " (director/story)" in x:
        return (x.split(' (director/story);')[-1]).split(', ')[0]
    elif " (director/writer)" in x:
        return (x.split(' (director/writer);')[-1]).split(', ')[0]
    elif " (directors)" in x:
        return (x.split(' (directors);')[-1]).split(', ')[0]
        
df_2016['actor_1_name']=df_2016['Cast and crew'].apply(lambda x:actor1(str(x)))


def actor2(x):
    if " (screenplay)" in x and len((x.split(' (screenplay);')[-1]).split(', '))>=2:
        return (x.split(' (screenplay);')[-1]).split(', ')[1]
    elif "  (screenplay)" in x and len((x.split(' (screenplay);')[-1]).split(', '))<2:
        return np.nan
    if " (director)" in x and len((x.split(' (director);')[-1]).split(', '))>=2:
        return (x.split(' (director);')[-1]).split(', ')[1]
    elif " (director/screenplay)" in x and len((x.split(' (director/screenplay);')[-1]).split(', '))>=2:
        return (x.split(' (director/screenplay);')[-1]).split(', ')[1]
    elif " (directors/screenplay)" in x and len((x.split(' (directors/screenplay);')[-1]).split(', '))>=2:
        return (x.split(' (directors/screenplay);')[-1]).split(', ')[1]
    elif " (director/story)" in x and len((x.split(' (director/story);')[-1]).split(', '))>=2:
        return (x.split(' (director/story);')[-1]).split(', ')[1]
    elif " (director/writer)" in x and len((x.split(' (director/writer);')[-1]).split(', '))>=2:
        return (x.split(' (director/writer);')[-1]).split(', ')[1]
    elif " (directors)" in x and len((x.split(' (directors);')[-1]).split(', '))>=2:
        return (x.split(' (directors);')[-1]).split(', ')[1]
    

df_2016['actor_2_name']=df_2016['Cast and crew'].apply(lambda x:actor2(str(x)))


def actor3(x):
    if " (screenplay)" in x and len((x.split(' (screenplay);')[-1]).split(', '))>=3:
        return (x.split(' (screenplay);')[-1]).split(', ')[2]
    elif "  (screenplay)" in x and len((x.split(' (screenplay);')[-1]).split(', '))<3:
        return np.nan
    if " (director)" in x and len((x.split(' (director);')[-1]).split(', '))>=3:
        return (x.split(' (director);')[-1]).split(', ')[2]
    elif " (director/screenplay)" in x and len((x.split(' (director/screenplay);')[-1]).split(', '))>=3:
        return (x.split(' (director/screenplay);')[-1]).split(', ')[2]
    elif " (directors/screenplay)" in x and len((x.split(' (directors/screenplay);')[-1]).split(', '))>=3:
        return (x.split(' (directors/screenplay);')[-1]).split(', ')[2]
    elif " (director/story)" in x and len((x.split(' (director/story);')[-1]).split(', '))>=3:
        return (x.split(' (director/story);')[-1]).split(', ')[2]
    elif " (director/writer)" in x and len((x.split(' (director/writer);')[-1]).split(', '))>=3:
        return (x.split(' (director/writer);')[-1]).split(', ')[2]
    elif " (directors)" in x and len((x.split(' (directors);')[-1]).split(', '))>=3:
        return (x.split(' (directors);')[-1]).split(', ')[2]
    




df_2016['actor_3_name']=df_2016['Cast and crew'].apply(lambda x:actor3(str(x)))


new_df16=df_2016.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]
new_df16.isna().sum()
new_df16.dropna(how='all',inplace=True)

new_df16['actor_2_name'] = new_df16['actor_2_name'].replace(np.nan, 'unknown')
new_df16['actor_3_name'] = new_df16['actor_3_name'].replace(np.nan, 'unknown')
new_df16['movie_title'] = new_df16['movie_title'].str.lower()
new_df16['combo'] = new_df16['actor_1_name'] + ' ' + new_df16['actor_2_name'] + ' '+ new_df16['actor_3_name'] + ' '+ new_df16['director_name'] +' ' + new_df16['genres']

old=pd.read_csv('../datasets/data.csv')
new_data=old.append(new_df16)
new_data.to_csv('../datasets/dataupto16.csv',index=False)

 


