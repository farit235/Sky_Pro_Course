# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from HW_18.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, g_id):
        return self.dao.get_one(g_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        g_id = data.get("id")
        director = self.get_one(g_id)
        director.id = data.get('id')
        director.name = data.get('name')
        self.dao.update(data)

    def update_partial(self, data):
        g_id = data.get("id")
        director = self.get_one(g_id)
        if "id" in data:
            director.id = data.get('id')
        if "name" in data:
            director.title = data.get('name')
        self.dao.update(data)

    def delete(self, g_id):
        self.dao.delete(g_id)
