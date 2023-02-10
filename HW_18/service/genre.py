from HW_18.dao.genre import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, g_id):
        return self.dao.get_one(g_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        g_id = data.get("id")
        genre = self.get_one(g_id)
        genre.id = data.get('id')
        genre.name = data.get('name')
        self.dao.update(data)

    def update_partial(self, data):
        g_id = data.get("id")
        genre = self.get_one(g_id)
        if "id" in data:
            genre.id = data.get('id')
        if "name" in data:
            genre.title = data.get('name')
        self.dao.update(data)

    def delete(self, g_id):
        self.dao.delete(g_id)
