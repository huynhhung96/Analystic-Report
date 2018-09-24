
import pandas
import numpy
import json
import matplotlib.pyplot

def load_tmdb_movies(path):
    df = pandas.read_csv(path)
    df = df.drop_duplicates()
    df['release_date'] = pandas.to_datetime(df['release_date']).apply(lambda x: x.date())
    json_columns = ['genres', 'keywords', 'production_countries', 'production_companies', 'spoken_languages']
    for column in json_columns:
        df[column] = df[column].apply(json.loads)
    return df
data = load_tmdb_movies('Downloads/tmdb_5000_movies.csv')

data

data.describe().round() #Describe numeric data type

def pipe_flatten_names(keywords):                  #Function collect genres name from Genres column
    return '|'.join([x['name'] for x in keywords])

data['genres'] = data['genres'].apply(pipe_flatten_names)

liste_genres = set()                               #Combine all the genres collected into a list
for s in data['genres'].str.split('|'):
    liste_genres = set().union(s, liste_genres)
liste_genres = list(liste_genres)
liste_genres.remove('')

data

data_reduced = data[['title','vote_average','release_date','runtime','budget','revenue']].reset_index(drop=True)

for genre in liste_genres:            #Map the genres list into a series of column
    data_reduced[genre] = data['genres'].str.contains(genre).apply(lambda x:1 if x else 0)    #If a film has that genres, the value is 1, else is 0

data_reduced.head()

mean_per_genre = pandas.DataFrame(liste_genres)         #Create a table contain the correlation between genres and vote average values
newArray = []*len(liste_genres)
for genre in liste_genres:
    newArray.append(df_reduced.groupby(genre, as_index=True)['vote_average'].mean())
newArray2 = []*len(liste_genres)
for i in range(len(liste_genres)):
    newArray2.append(newArray[i][1])

mean_per_genre['mean_votes_average']=newArray2

data_use.plot(kind='scatter', x='year', y='revenue', alpha=.5, color='r')         #Scatter plot of values of revenue and release date
plt.xlabel('year')
plt.ylabel('revenue')
plt.title('Scatter Plot')
plt.show()
