import requests
import json

def get_movie_info(movie):

    headers = {
        "x-rapidapi-key": "b690d7766amshd66d0e72dd0b864p12f7c9jsnd8d77185aaaf",
        "x-rapidapi-host": "movie-database-alternative.p.rapidapi.com"
    }

    url = "https://movie-database-alternative.p.rapidapi.com/"
    
    querystring = {"s":movie}
    response = requests.get(url, headers=headers, params=querystring)
    
    response_json = response.json()

    movie_info = response_json["Search"]

    for x in movie_info:
        print (x["Title"], x["Year"])

    with open('movies.json', 'w') as f:
        json.dump (response_json, f)