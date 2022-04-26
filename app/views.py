from flask import render_template
from app import app
from .request import get_movies

#views
@app.route('/')
def index():
    #getting popular movies
    popular_movies = get_movies('popular')
    print(popular_movies)
    message = "Hello Flask"
    title = 'Home: Welcome to the bestMovie review website online!'
    return render_template('index.html',message = message, title = title, popular = popular_movies)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    return render_template('movie.html',id = movie_id)