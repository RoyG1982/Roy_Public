import movie_local_file
import movie_api
import argparse
import json

with open ("movies.json", "r") as f:
    current_info = json.load(f)

current_movie_info = current_info["Search"]

def print_info_from_file(movie):
    for x in current_movie_info:
        if x ["Title"] == movie:
            print(x ["Title"], x["Year"])

parser = argparse.ArgumentParser()
parser.add_argument ("-s", "--movie", type = str, required = True)
movie = parser.parse_args().movie

def main(movie):
    if movie_local_file.is_in_file(movie) == True:
        print ("found movie locally")
        print_info_from_file(movie)
    else:
        print ("not found locally")
        movie_api.get_movie_info(movie)

main(movie)
