from mongo_data.Models.movies import Movie


def store_movies(lines):
    for line in lines:
        line['_id'] = line['movie_id']
        del line['movie_id']
        movie = Movie(**line)
        movie.save()


def get_all():
    return Movie.get_all()


def find(**kwargs):
    return Movie.find(**kwargs)