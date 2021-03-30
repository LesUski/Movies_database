import sqlalchemy

from sql_data.Models.movies import Movie, Genre, Character
from sql_data.db import session, engine


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
    con = engine.connect()
    sql = "SELECT * FROM movies_genres"
    result = con.execute(sql)

    for row in result:
        movie_id = row[0]
        genre_id = row[1]
        genre = session.query(Genre).filter(Genre.genre_id==genre_id).first()
        first_genre = session.query(Genre).filter(Genre.genre_name==genre.genre_name).first()
        if genre_id != first_genre.genre_id:
            try:
                sql = f"UPDATE movies_genres SET genres_genre_id={first_genre.genre_id} WHERE movies_movie_id='{movie_id}' AND genres_genre_id={genre_id}"
                con.execute(sql)
            except sqlalchemy.exc.IntefrityError as e:
                sql = f"DELETE FROM movies_genres WHERE movies_movie_id='{movie_id}' AND genres_genre_id={genre_id}"
                con.execute(sql)


def delete_duplicate_genres():
    con = engine.connect()
    sql = "SELECT DISTINCT genres_genre_id FROM movies_genres"
    genre_ids = [value[0] for value in con.execute(sql)]
    for genre in session.query(Genre).all():
        if genre.genre_id not in genre_ids:
            sql = f"DELETE FROM genres WHERE genre_id={genre.genre_id}"
            con.execute(sql)

