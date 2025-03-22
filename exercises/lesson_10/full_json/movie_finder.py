import json
import requests

def get_movie_info(movie):

    headers = {
        "x-rapidapi-key": "b690d7766amshd66d0e72dd0b864p12f7c9jsnd8d77185aaaf",
        "x-rapidapi-host": "movie-database-alternative.p.rapidapi.com"
    }

    url = "https://movie-database-alternative.p.rapidapi.com/"
    
    querystring = {"s":movie}
    response = requests.get(url, headers=headers, params=querystring)
    
    return response.json()