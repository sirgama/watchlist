from flask import render_template
from app import app

#views
@app.route('/')
def index():
    message = "Hello Flask"
    title = 'Home: Welcome to the bestMovie review website online!'
    return render_template('index.html',message = message, title = title)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    return render_template('movie.html')