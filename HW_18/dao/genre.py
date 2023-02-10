from HW_18.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, g_id):
        return self.session.query(Genre).get(g_id)

    def create(self, data):
        new_genre = Genre(**data)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, g_id):
        genre = self.get_one(g_id)
        self.session.delete(genre)
        self.session.commit()
