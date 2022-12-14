import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


def get_all_titles(soup):
    result_topics=[]
    all_topics=soup.find_all('h3',{"class":"lister-item-header"}) #see from webpage inspect 
    # print(all_topics)
    for topic in all_topics:
        topic=str(topic.find('a'))
        topic=topic.replace("<","=")
        topic=topic.replace(">","=")
        topic=topic.split('=')
        topic=topic[int(len(topic)/2)]
        result_topics.append(topic)
    print(result_topics)
    return result_topics

def get_all_genres(soup):
    result_genres=[]
    all_genres=soup.find_all("p",{"class":"text-muted"})
    print(all_genres)
    for genre in all_genres:
        genre=str(genre.find_all("span",{"class":"genre"}))
        if genre=='[]':
            pass
        else:
            genre=genre.replace("<","=")
            genre=genre.replace(">","=")
            genre=genre.split('=')
            genre=genre[int(len(genre)/2)]
            result_genres.append(genre)
    print(result_genres)
    return result_genres

def post_process(genre):
    post_process_genres=[]
    for i in genre:
        i=i.replace("\n","")
        i=i.replace(" ","")
        post_process_genres.append(i)
    print(post_process_genres)
    return post_process_genres

def check_repeated_comma(x):
    list_x=x.split(',')
    if len(list_x)==3:
        return x
    else:
        return np.nan

def data_set(url):
    data_set= pd.DataFrame(columns= ["Movie","Primary Genre","Secondary Genre", "Tertiary Genre"])
    #initially get the page from the url and from the content extract all the things properly so page is extracted
    page=requests.get(url)
    #Soup is created where all the content is pared as html format so it can be extracted as seen in webpages
    soup= BeautifulSoup(page.content,'html.parser')
    # print(soup)
    title= get_all_titles(soup)
    genres=get_all_genres(soup)
    genres=post_process(genres)
    data_set["Movie"]=pd.Series(title)
    data_set["Primary Genre"]=pd.Series(genres)
    data_set["Primary Genre"]=data_set["Primary Genre"].apply(check_repeated_comma)
    print(data_set)
    data_set["Secondary Genre"]=data_set["Secondary Genre"].fillna('To Be Filled')
    data_set["Tertiary Genre"]=data_set['Tertiary Genre'].fill5na('To Be Filled')
    data_set=data_set.loc[data_set['Primary Genre']!=np.NaN]
    data_set=data_set.dropna(how="any")
    data_set[["Primary Genre","Seconday Genre","Tertiary Genre"]]=data_set["Primary Genre"].str.split(',',expand=True)
    data_set.to_csv("Dataset",mode='a',header=False)


import os
os.system('cls')
print('IMDB Scrapper')
number_of_pages=int(input('Enter the number of various pages to scap: '))
# page = 1
for i in range(number_of_pages):
    url=input('Enter the url: ')
    
    data_set(url)
    
