from HW_19.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, u_id):
        return self.session.query(User).get(u_id)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, u_id):
        user = self.get_one(u_id)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        user = self.get_one(user_data.get('id'))
        user.username = user_data.get('username')
        user.password = user_data.get('password')
        user.role = user_data.get('role')

        self.session.add(user)
        self.session.commit()
