import pandas as pd


def assign_genre_values(df):
    p= df.to_list()
    p=set(p)
    # print (p)

    dictionary={}
    count=0
    for value in p:
        dictionary[value]=count
        count+=1
    for index in range(0,df.shape[0]):
        try: 
            if df[index] in dict.keys(dictionary):
                df[index]=dictionary[df[index]]
        except:
            pass
    return df

def pre_process_all():
    df=pd.DataFrame()
    df=pd.read_csv('Dataset.csv')
    df.columns=['S.N','Movie','P_Genre','remove','S_Genre','T_Genre']
    df.pop('remove')
    df['Movie']=df['Movie'].str.lower()
    df.drop_duplicates(subset='Movie',keep='first',inplace=True)
    df['Movie']=df['Movie'].str.replace("  "," ")
    df=df.drop(['S.N'],axis=1)
    Genres=['P_Genre','S_Genre','T_Genre']
    for Genre in Genres:
        df[Genre]=assign_genre_values(df[Genre])
    return df
    
pre_process_all()