from sql_data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

# movies_genres = sa.Table('movies_genres', Base.metadata,
#                          sa.Column('movies_movie_id', sa.String(5), sa.ForeignKey('movies.movie_id')),
#                          sa.Column('genres_genre_id', sa.Integer, sa.ForeignKey('genres.genre_id'))
#                          )


# movie_lines = sa.Table('movie_lines', Base.metadata,
#                        sa.Column('characters_character_id', sa.String(6), sa.ForeignKey('characters.character_id')),
#                        sa.Column('movies_movie_id', sa.String(5), sa.ForeignKey('movies.movies_id')))
#

class MovieGenre(Base):
    __tablename__ = 'movies_genres'

    movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), primary_key=True)
    genres_genre_id = sa.Column(sa.Integer, sa.ForeignKey('genres.genre_id'), primary_key=True)

    genre = relationship('Genre', back_populates='movies')
    movie = relationship('Movie', back_populates='genres')


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = sa.Column(sa.String(5), primary_key=True)
    movie_title = sa.Column(sa.String(200), nullable=False)
    movie_year = sa.Column(sa.Integer, nullable=False)
    imdb_rating = sa.Column(sa.Float, nullable=False)
    imdb_votes = sa.Column(sa.Integer, nullable=False)

    characters = relationship("Character")
    genres = relationship("MovieGenre", back_populates='movie')

    def __repr__(self):
        return f'{self.movie_title} - {self.movie_year}'


class Genre(Base):
    __tablename__ = 'genres'

    genre_id = sa.Column(sa.Integer, primary_key=True)
    genre_name = sa.Column(sa.String(105), nullable=False)

    movies = relationship('MovieGenre', back_populates='genre')

    def __repr__(self):
        return self.genre_name


class Character(Base):
    __tablename__ = 'characters'

    character_id = sa.Column(sa.String(6), primary_key=True)
    character_name = sa.Column(sa.String(150), nullable=False)
    gender = sa.Column(sa.String(5), nullable=True)
    movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), nullable=False)

    def __repr__(self):
        return f'{self.character_name}: '
