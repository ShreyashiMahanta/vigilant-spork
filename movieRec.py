from flask import Flask,jsonify,request
import csv
import shutil
import os.path

allMovies = []

with open('movies.csv',encoding='UTF8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

likedMovies = []
notLikedMovies = []
didNotWatchMovies = []

app = Flask(__name__)

@app.route('/get-movie')

def get_movie():
    return jsonify({
        'data' : allMovies[0],
        'status' : 'success'
    })

@app.route('/liked-movies',methods=['POST'])

def likedMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        'status' : 'success'
    }),201

@app.route('/unliked-movies',methods=['POST'])

def unlikedMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    notLikedMovies.append(movie)
    return jsonify({
        'status' : 'success'
    }),201

@app.route('/not-watched-movies',methods=['POST'])

def didNotWatchMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    didNotWatchMovies.append(movie)
    return jsonify({
        'status' : 'success'
    }),201



if __name__ == '__main__':
    app.run()



