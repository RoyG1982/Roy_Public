import json

with open ("movies.json", "r") as f:
    current_info = json.load(f)

current_movie_info = current_info["Search"]

def is_in_file(movie):
    for x in current_movie_info:
        if x ["Title"] == movie:
            return True
        return False