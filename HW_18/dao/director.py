from HW_18.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, d_id):
        return self.session.query(Director).get(d_id)

    def create(self, data):
        new_director = Director(**data)
        self.session.add(new_director)
        self.session.commit()
        return new_director

    def update(self, director):
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, d_id):
        director = self.get_one(d_id)
        self.session.delete(director)
        self.session.commit()
