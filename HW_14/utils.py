import json
import sqlite3


def find_movie_by_name(title):
    """Функция поиска фильма по названию"""
    query = f"""
            SELECT title, country, release_year, listed_in, description \
            FROM netflix \
            WHERE title LIKE '%{title}%' \
            AND date_added IS NOT NULL \
            ORDER BY release_year DESC
            LIMIT 1 
            """

    with sqlite3.connect("HW_14/netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            movie = {"title": row[0], "country": row[1], "release_year": row[2],
                     "genre": row[3], "description": row[4]}

    return movie


def find_movie_by_years(from_, to_):
    """Функция поиска по диапазону лет"""
    query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {from_} AND {to_}
            LIMIT 100
            """

    lst_movie = []

    with sqlite3.connect("HW_14/netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            movie = {"title": row[0], "release_year": row[1]}
            lst_movie.append(movie)

    return lst_movie


def find_movie_by_age_limits(rating):
    """Функция поиска по возрастному рейтингу"""
    if rating == 'children':
        rating_lst = "'G'"
    elif rating == 'family':
        rating_lst = "'G', 'PG', 'PG-13'"
    elif rating == 'adult':
        rating_lst = "'R', 'NC-17'"
    else:
        rating_lst = "'G', 'PG', 'PG-13', 'R', 'NC-17'"

    query = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating IN ({rating_lst})
            """

    lst_movies = []

    with sqlite3.connect('HW_14/netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            movie = {"title": row[0], "rating": row[1], "description": row[2]}
            lst_movies.append(movie)
    return lst_movies


def find_movie_by_genre(genre):
    """Функция поиска по жанру"""
    query = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
            """

    lst_movies = []

    with sqlite3.connect('HW_14/netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            movie = {"title": row[0], "description": row[1]}
            lst_movies.append(movie)
        movies = json.dumps(lst_movies)

    return movies


def search_couple_in_casts(actor_1, actor_2):
    """Функция поиска актеров, которые играют в парах"""
    query = """
            SELECT "cast"
            FROM netflix
            """

    couple_actors = []

    with sqlite3.connect("HW_14/netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            if row[0] is None:
                continue
            else:
                lst_names = row[0].split(",")
                if actor_1 in lst_names and actor_2 in lst_names:
                    for name in lst_names:
                        if name != actor_1 and name != actor_2:
                            couple_actors.append(name)

    return list(set(couple_actors))


def find_movie_by_type_year_genre(type_, year_, genre_):
    """Функция поиска фильма по типу, году и жанру"""
    query = f"""
            SELECT title, description
            FROM netflix
            WHERE type = '{type_}'
            AND release_year = '{year_}'
            AND listed_in LIKE '%{genre_}%'
            """

    lst_movies = []

    with sqlite3.connect("HW_14/netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            movie = {"title": row[0], "description": row[1]}
            lst_movies.append(movie)
    movies = json.dumps(lst_movies)
    return movies


print(search_couple_in_casts("Jack Black", " Dustin Hoffman"))
print(find_movie_by_type_year_genre("TV Show", "2020", "Drama"))
