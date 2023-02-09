from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(app)
movie_ns = api.namespace("/movies/")
director_ns = api.namespace("/directors/")
genre_ns = api.namespace("/genres/")


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if director_id:
            all_movies = Movie.query.filter(Movie.director_id == director_id).all()
        elif genre_id:
            all_movies = Movie.query.filter(Movie.genre_id == genre_id).all()
        elif director_id and genre_id:
            all_movies = Movie.query.filter(Movie.director_id == director_id and Movie.genre_id == genre_id).all()
        else:
            all_movies = Movie.query.all()
        return movies_schema.dumps(all_movies), 200

    def post(self):
        data = request.json
        new_movie = Movie(**data)
        db.session.add(new_movie)
        db.session.commit()
        db.session.close()
        return '', 201


@movie_ns.route("/<int:m_id>")
class MoviesView(Resource):
    def get(self, m_id: int):
        movie = Movie.query.get(m_id)
        return movie_schema.dumps(movie), 200

    def put(self, m_id: int):
        data = request.get_json()
        movie = Movie.query.get(m_id)
        movie.id = data['id']
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        db.session.add(movie)
        db.session.commit()
        db.session.close()
        return '', 201

    def delete(self, m_id: int):
        movie = Movie.query.get(m_id)
        db.session.delete(movie)
        db.session.commit()
        return '', 204


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        return directors_schema.dumps(directors), 200

    def post(self):
        data = request.json
        new_director = Director(**data)
        db.session.add(new_director)
        db.session.commit()
        db.session.close()
        return '', 201


@director_ns.route('/<int:d_id>')
class DirectorView(Resource):
    def get(self, d_id: int):
        directors = Director.query.get(d_id)
        return director_schema.dumps(directors), 200

    def put(self, d_id: int):
        director = Director.query.get(d_id)
        data = request.json
        director.id = data['id']
        director.name = data['name']
        db.session.add(director)
        db.session.commit()
        db.session.close()
        return '', 200

    def delete(self, d_id: int):
        director = Director.query.get(d_id)
        db.session.delete(director)
        db.session.commit()
        db.session.close()

        return '', 204


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = Genre.query.all()
        return genres_schema.dumps(genres), 200

    def post(self):
        data = request.json
        new_genre = Genre(**data)
        db.session.add(new_genre)
        db.session.commit()
        db.session.close()
        return '', 201


@genre_ns.route("/<int:g_id>")
class GenreView(Resource):
    def get(self, g_id: int):
        genre = Genre.query.get(g_id)
        return genre_schema.dumps(genre), 200

    def put(self,  g_id: int):
        genre = Genre.query.get(g_id)
        data = request.json
        genre.id = data["id"]
        genre.name = data["name"]
        db.session.add(genre)
        db.session.commit()
        db.session.close()
        return '', 201

    def delete(self, g_id: int):
        genre = Genre.query.get(g_id)
        db.session.delete(genre)
        db.session.commit()
        db.session.close()
        return '', 204


if __name__ == '__main__':
    app.run(debug=True)
