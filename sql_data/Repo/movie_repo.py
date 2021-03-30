from sql_data.Models.movies import Movie, Genre, Character
from sql_data.db import session


def store_movies(lines):
    for line in lines:
        # del line['genres']
        line['genres'] = [Genre(genre_name=genre) for genre in line['genres']]
        movie = Movie(**line)
        session.add(movie)
    session.commit()


def store_characters(characters):
    for line in characters:
        line['gender'] = line['gender'] if line['gender'] != '?' else None
        character = Character(**line)
        session.add(character)
    session.commit()


def get_movie_by_id(id):
    return session.query(Movie).filter(Movie.movie_id == id).first()


def fix_genres():
