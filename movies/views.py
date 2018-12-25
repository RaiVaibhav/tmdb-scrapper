from configparser import ConfigParser
from django.shortcuts import render
import tmdbsimple as tmdb
import os

tmdb.API_KEY = str(os.environ['API_KEY'])
def home(request):
    return render(request, "base.html")

def movie_list(request):
    query = str(request.POST.get('search_text', ''))
    if query != '':
        search_result = tmdb.Search().movie(query=query)['results']
        frontend = {
            "search_result": sorted(search_result, key=lambda x: x['popularity'], reverse=True),
            "has_result": (search_result != [])
        }
    else:
        frontend = {
            "search_result": [],
            "has_result": False
        }
    return render(request, "ajax_search.html", frontend)

def details(request, id=None):
    movie = tmdb.Movies(id)
    trailers = list(filter(lambda v: v['type'] == 'Trailer', movie.videos()['results']))
    teasers = list(filter(lambda v: v['type'] == 'Teaser', movie.videos()['results']))
    keywords = movie.keywords()['keywords']
    frontend = {
        "info": movie.info(),
        "year": movie.info()['release_date'][:4],
        "cast": movie.credits()['cast'][:15],
        "crew": movie.credits()['crew'][:15],
        "trailers": trailers,
        "teasers": teasers,
        "keywords": keywords,
        "reviews": movie.reviews()['results'],
        "alt": movie.alternative_titles()['titles'],
    }
    return render(request, "details.html", frontend)
