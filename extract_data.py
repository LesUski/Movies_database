from sql_data.Repo.movie_repo import store_characters
from mongo_data.Repo.movie_repo import *


def extract_movie_data():
    with open('raw_data/movie_titles_metadata.txt') as movie_data:
        lines = []
        genres = set()
        for line in movie_data:
            line = line.strip()
            line_data = line.split(' +++$+++ ')
            line_dict = {
                'movie_id': line_data[0],
                'movie_title': line_data[1].title(),
                'movie_year': int(line_data[2]),
                'imdb_rating': float(line_data[3]),
                'imdb_votes': int(line_data[4]),
                'genres': line_data[5][1:-2].replace("'", "").split(', ')
            }
            for genre in line_dict['genres']:
                genres.add(genre)
            lines.append(line_dict)

    store_movies(lines)


def extract_character_data():
    with open('raw_data/movie_characters_metadata.txt') as char_data:
        characters = []
        for line in char_data:
            line = line.strip()
            line_data = line.split(' +++$+++ ')
            line_dict = {
                'character_id': line_data[0],
                'character_name': line_data[1].title(),
                'movies_movie_id': line_data[2],
                'gender': line_data[4]
            }
            characters.append(line_dict)

    store_characters(characters)


def extract_movie_lines():
    with open('raw_data/movie_lines.txt') as lines_data:
        lines = []
        for line in lines_data:
            line = line.strip()
            line_data = line.split(' +++$+++ ')
            print(line_data)
            line_dict = {
                'line_id': line_data[0],
                'line_text': line_data[4]
            }
        lines.append(line_dict)
        #print(lines)


def main():
    # extract_movie_data()
    extract_character_data()
    # extract_movie_lines()

    # all_movies = find(movie_year=1994)
    # print(all_movies)


if __name__ == '__main__':
    main()
