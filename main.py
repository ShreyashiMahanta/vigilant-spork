from flask import Flask,jsonify, request
from movieRec import likedMovies,notLikedMovies,didNotWatchMovies,allMovies
from demographic_filtering import output
from contentFiltering import get_reccomendation

app = Flask(__name__)

@app.route('/get-movie')

def get_movie():
    movie_data = {
        'title': allMovies[0][19],
        'poster_link' : allMovies[0][27],
        'release_data' : allMovies[0][13] or 'n/a',
        'duration' : allMovies[0][15],
        'rating' : allMovies[0][20],
        'overview' : allMovies[0][9],
    }
    return jsonify({
        'data': movie_data,
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

@app.route('/popular-movies')

def popularMovies():
    movieData = []
    for movie in output:
        d = {
            'title' : movie[0],
            'poster_link' : movie[1],
            'release_data' : movie[2],
            'duration' : movie[3],
            'rating' : movie[4],
            'overview' : movie[5],
        }
        movieData.append(d)
    return jsonify({
        'data' : movieData,
        'status' : 'success'
    }),200

if __name__ == '__main__':
    app.run()