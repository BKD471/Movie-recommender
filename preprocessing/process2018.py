# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 02:29:06 2021

@author: User
"""
import pandas as pd
import numpy as np

link_2018='https://en.wikipedia.org/wiki/List_of_American_films_of_2018'
df1=pd.read_html(link_2018,header=0)[2]
df2=pd.read_html(link_2018,header=0)[3]
df3=pd.read_html(link_2018,header=0)[4]
df4=pd.read_html(link_2018,header=0)[5]

df=df1.append(df2.append(df3.append(df4,ignore_index=True),ignore_index=True),ignore_index=True)

from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests
import json
tmdb=TMDb()
tmdb.api_key='2c4a17a043d93c60bd7f3fd7b0c00958'
tmdb_movie=Movie()
def get_genre(x):
    genre=[]
    result=tmdb_movie.search(x)
    movie_id=result[0].id
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
    data=response.json()
    if data['genres']:
        n=len(data['genres'])
        for i in range(n):
            genre.append(data['genres'][i]['name'])
        return ' '.join(genre)
    else:    
        return np.nan
    
df['genres']=df['Title'].apply(lambda x:get_genre(str(x)))

df=df.loc[:,['Title','Cast and crew','genres']]

df=df.rename(columns={'Title':'movie_title'})

def get_director(x):
    if " (director)" in x:
        return x.split(" (director)")[0]
    elif " (directors)" in x:
        return x.split(" (directors)")[0]
    elif " (directors/screenplay)" in x:
        return x.split(" (directors/screenplay)")[0]
    elif "(director/​screenplay)" in x:
        return x.split("(director/​screenplay)")[0]
    else:
        return x.split("(director/screenplay)")[0]
   
    
df['director_name']=df['Cast and crew'].apply(lambda x:get_director(str(x)))

def act1(x):
    if " (screenplay)" in x:
        return (x.split(' (screenplay);')[-1]).split(', ')[0]
    elif " (co-director/screenplay)" in x:
        return (x.split(' (co-director/screenplay);')[-1]).split(', ')[0]
    elif " (writer)" in x:
        return (x.split(' (writer);')[-1]).split(', ')[0]
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
    
df['actor_1_name']=df['Cast and crew'].apply(lambda x:act1(str(x)))


def act2(x):
    
    if "(screenplay)" in x and len((x.split('(screenplay);')[-1]).split(','))>=2:
        return (x.split('(screenplay);')[-1]).split(',')[1]
    elif "(screenplay)" in x and len((x.split('(screenplay);')[-1]).split(', '))<2:
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

df['actor_2_name']=df['Cast and crew'].apply(lambda x:act2(str(x)))   
 

def act3(x):
    if "(screenplay)" in x and len((x.split('(screenplay);')[-1]).split(','))>=3:
        return (x.split(' (screenplay);')[-1]).split(', ')[2]
    elif "(screenplay)" in x and len((x.split('(screenplay);')[-1]).split(','))<3:
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
        
df['actor_3_name']=df['Cast and crew'].apply(lambda x:act3(str(x)))

df_18=df.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]

df_18.isna().sum()

df_18['actor_2_name']=df['actor_2_name'].replace(np.nan,'unknown')
df_18['actor_3_name']=df['actor_3_name'].replace(np.nan,'unknown')

df_18['movie_title']=df_18['movie_title'].str.lower()

df_18['combo']=df_18['actor_1_name']+" "+df_18['actor_2_name']+" "+df_18['actor_3_name']+" "+df_18['director_name']+" "+df_18['genres']

old=pd.read_csv('../datasets/dataupto17.csv')

new_data=old.append(df_18)


new_data.to_csv('../datasets/dataupto18.csv',index=False)

    
