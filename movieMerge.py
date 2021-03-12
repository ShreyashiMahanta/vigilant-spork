import pandas as pd
import csv

with open('movies.csv',encoding='UTF8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
    headers = data[0]

headers.append('poster_link')

with open('final.csv','a+') as f:
    csv.writer = csv.writer(f)
    csv.writer.writerow(headers)

with open('movie_links.csv',encoding='UTF8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovieLinks = data[1:]

for movie_item in allMovies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in allMovieLinks)
    if poster_found:
        for movie_link_item in allMovieLinks:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open('final.csv','a+') as f:
                        csv.writer = csv.writer(f)
                        csv.writer.writerow(movie_item)