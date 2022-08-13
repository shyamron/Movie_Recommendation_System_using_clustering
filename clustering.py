import preprocessing
from sklearn.cluster import KMeans


def final_df(df):
    df['Cluster_ID']=None

    kmeans=KMeans(n_clusters=200)
    features=df[['P_Genre','S_Genre','T_Genre']]
    kmeans.fit(features)
    df['Cluster_ID'] = kmeans.predict(features)
    return df 

def cluster(input_movie):
    df=preprocessing.pre_process_all()
    print(df)
    df=final_df(df)
    df.to_csv('Dataset_to_plot.csv')
    # check if the movie is present or not 
    input_movie = input_movie.lower() 
    try:
        movie_not_found = df.loc[~df['Movie'].str.contains(input_movie)]
        if len(movie_not_found) == 0:
            print('Movie not found')
            return 0
        get_cluster = df['Cluster_ID'].loc[df['Movie'].str.contains(input_movie)].values[0]
        similar_movies_list = df['Movie'].loc[df['Cluster_ID']==get_cluster].values 
        return similar_movies_list
    except:
        print('Movie not found')
        return 0