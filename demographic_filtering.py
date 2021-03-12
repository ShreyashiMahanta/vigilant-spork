import pandas as pd
import numpy as np

df = pd.read_csv('final.csv')

c = df['vote_average'].mean()
print(c)

m = df['vote_count'].quantile(0.9)
print(m)

QMovies = df.copy().loc[df['vote_count']>= m]
print(QMovies.shape)

def weightedRating(x,m = m,c = c):
  v = x['vote_count']
  r = x['vote_average']
  return (v/(v+m)*r)+(m/(m+v)*c)

QMovies['score'] = QMovies.apply(weightedRating,axis=1)

QMovies = QMovies.sort_values('score',ascending= False)
output = QMovies[['original_title','vote_count','vote_average','score']].head(10).values.tolist()
print(output)