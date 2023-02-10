from HW_18.dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, m_id):
        return self.dao.get_one(m_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        m_id = data.get("id")
        movie = self.get_one(m_id)
        movie.id = data.get('id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.dao.update(data)

    def update_partial(self, data):
        m_id = data.get("id")
        movie = self.get_one(m_id)
        if "id" in data:
            movie.id = data.get('id')
        if "title" in data:
            movie.title = data.get('title')
        if "description" in data:
            movie.description = data.get('description')
        if "trailer" in data:
            movie.trailer = data.get('trailer')
        if "year" in data:
            movie.year = data.get('year')
        if "rating" in data:
            movie.rating = data.get('rating')
        if "genre_id" in data:
            movie.genre_id = data.get('genre_id')
        if "director_id" in data:
            movie.director_id = data.get('director_id')
        self.dao.update(data)

    def delete(self, m_id):
        self.dao.delete(m_id)
