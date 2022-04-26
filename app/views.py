from flask import render_template
from app import app

#views
@app.route('/')
def index():
    return render_template('index.html',message = "message")

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html',id = movie_id)