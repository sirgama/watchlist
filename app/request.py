from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie


#getting api key

api_key = app.config['MOVIE_API_KEY']

#getting the movie base url
base_url = app.config['MOVIE_API_BASE_URL']

def process_results(movie_list):
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        
        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)
    
    return movie_results