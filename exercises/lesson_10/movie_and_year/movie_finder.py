import json
import requests

import json
import requests

def get_movie_info(movie):
    headers = {
        "x-rapidapi-key": "b690d7766amshd66d0e72dd0b864p12f7c9jsnd8d77185aaaf",
        "x-rapidapi-host": "movie-database-alternative.p.rapidapi.com"
    }

    url = "https://movie-database-alternative.p.rapidapi.com/"

    querystring = {"s": movie}
    response = requests.get(url, headers=headers, params=querystring)

    # Check if the response is successful and contains the 'Search' key
    data = response.json()
    
    # Ensure the response contains the 'Search' key
    if "Search" in data:
        return data["Search"]  # Return only the list of movies from the 'Search' key
    else:
        return []  # Return an empty list if no results are found or if there's an error
