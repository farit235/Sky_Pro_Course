import json
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSON_AS_ASCII"] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age > 0"))
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    customer = relationship("User", foreign_keys=customer_id)
    executor = relationship("User", foreign_keys=executor_id)


class Offer(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor = relationship("User")
    order = relationship("Order")


def main():
    db.create_all()
    insert_data()
    app.run(debug=True)


def insert_data():
    """Получение данных из json файлов в БД"""
    with open("json_data/users.json") as file:
        users_from_json = json.load(file)

    with open("json_data/offers.json") as file:
        offers_from_json = json.load(file)

    with open("json_data/orders.json") as file:
        orders_from_json = json.load(file)

    users = []
    offers = []
    orders = []

    for user in users_from_json:
        user_ = User(id=user['id'], first_name=user["first_name"], second_name=user["last_name"], age=user["age"],
                     email=user["email"], role=user["role"], phone=user["phone"])
        users.append(user_)

    for order in orders_from_json:
        order_ = Order(id=order['id'], name=order['name'], description=order["description"],
                       start_date=datetime.strptime(order["start_date"], '%m/%d/%Y'),
                       end_date=datetime.strptime(order["end_date"], '%m/%d/%Y'), address=order["address"],
                       price=order["price"], customer_id=order["customer_id"], executor_id=order["executor_id"])
        orders.append(order_)

    for offer in offers_from_json:
        offer_ = Offer(id=offer['id'], order_id=offer["order_id"], executor_id=offer["executor_id"])
        offers.append(offer_)

    with db.session.begin():
        db.session.add_all(users)
        db.session.add_all(orders)
        db.session.add_all(offers)


@app.route("/orders/", methods=['GET', 'POST'])
def get_all_orders():
    """Функция нахождения всех заказов через GET и через POST добавляет запись в БД"""
    if request.method == 'GET':
        order_response = []
        orders_list = Order.query.all()
        for order in orders_list:
            customer = User.query.get(order.customer_id).first_name if order.customer_id != 0 else 0
            executor = User.query.get(order.executor_id).first_name if order.executor_id != 0 else 0
            order_response.append({
                "id": order.id,
                "name": order.name,
                "description": order.description,
                "start_date": order.start_date,
                "end_date": order.end_date,
                "address": order.address,
                "price": order.price,
                "customer_id": customer,
                "executor_id": executor,
            })
        return json.dumps(order_response, ensure_ascii=False, default=str)

    elif request.method == 'POST':
        data = request.get_json()
        new_order = Order(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            start_date=datetime.strptime(data['start_date'], "%Y-%m-%d"),
            end_date=datetime.strptime(data['end_date'], "%Y-%m-%d"),
            address=data['address'],
            price=data['price'],
            customer_id=data['customer_id'],
            executor_id=data['executor_id']
        )

        db.session.add(new_order)
        db.session.commit()
        return '', 200


@app.route("/orders/<int:o_id>", methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(o_id):
    """Функция нахождения заказа через GET и через PUT обновляет данные в таблице, а через DELETE удаляет запись"""
    if request.method == 'GET':
        order = Order.query.get(o_id)
        order_data = {
            "id": order.id,
            "name": order.name,
            "description": order.description,
            "start_date": order.start_date,
            "end_date": order.end_date,
            "address": order.address,
            "price": order.price,
            "customer_id": order.customer_id,
            "executor_id": order.executor_id
        }
        return json.dumps(order_data, ensure_ascii=False, default=str)

    elif request.method == 'PUT':
        data = request.get_json()
        order = Order.query.get(o_id)
        order.name = data['name']
        order.description = data['description']
        order.start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
        order.end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
        order.address = data['address']
        order.price = data['price']
        order.customer_id = data['customer_id']
        order.executor_id = data['executor_id']

        db.session.add(order)
        db.session.commit()
        return '', 200

    elif request.method == 'DELETE':
        order = Order.query.get(o_id)
        db.session.delete(order)
        db.session.commit()
        return '', 200


@app.route("/users/", methods=['GET', 'POST'])
def get_all_users():
    """Функция нахождения всех пользователей через GET и через POST добавляет запись в БД"""
    if request.method == 'GET':
        user_response = []
        users_list = User.query.all()
        for user in users_list:
            user_response.append({
                "id": user.id,
                "first_name": user.first_name,
                "second_name": user.second_name,
                "age": user.age,
                "email": user.email,
                "role": user.role,
                "phone": user.phone
            })
        return json.dumps(user_response, ensure_ascii=False)

    elif request.method == 'POST':
        data = request.json
        user = User(
            id=data['id'],
            first_name=data['first_name'],
            second_name=data['second_name'],
            age=data['age'],
            email=data['email'],
            role=data['role'],
            phone=data['phone']
        )
        db.session.add(user)
        db.session.commit()
        return '', 200


@app.route("/users/<int:u_id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(u_id):
    """Функция нахождения пользователя через GET и через PUT обновляет данные в таблице, а через DELETE удаляет запись"""
    if request.method == 'GET':
        user = User.query.get(u_id)
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'second_name': user.second_name,
            'age': user.age,
            "email": user.email,
            "role": user.role,
            "phone": user.phone
        }
        return json.dumps(user_data, ensure_ascii=False)

    elif request.method == "PUT":
        data = request.json
        user = User.query.get(u_id)
        user.first_name = data['first_name']
        user.second_name = data['second_name']
        user.age = data['age']
        user.email = data['email']
        user.role = data['role']
        user.phone = data['phone']

        db.session.add(user)
        db.session.commit()
        return '', 200

    elif request.method == 'DELETE':
        user = User.query.get(u_id)
        db.session.delete(user)
        db.session.commit()
        return '', 200


@app.route("/offers/", methods=['GET', 'POST'])
def get_all_offers():
    """Функция нахождения всех офферов через GET и через POST добавляет запись в БД"""
    if request.method == 'GET':
        offers_list = []
        offers = Offer.query.all()
        for offer in offers:
            offers_list.append({
                'id': offer.id,
                'order_id': offer.order_id,
                'executor_id': offer.executor_id
            })
        return json.dumps(offers_list)

    elif request.method == 'POST':
        data = request.json
        new_offer = Offer(
            order_id=data['order_id'],
            executor_id=data['executor_id']
        )
        db.session.add(new_offer)
        db.session.commit()
        return '', 200


@app.route("/offers/<int:of_id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(of_id):
    """Функция нахождения оффера через GET и через PUT обновляет данные в таблице, а через DELETE удаляет запись"""
    if request.method == "GET":
        offer = Offer.query.get(of_id)
        offer_data = {
            'id': offer.id,
            'order_id': offer.order_id,
            'executor_id': offer.executor_id
        }
        return json.dumps(offer_data)

    elif request.method == 'PUT':
        new_data = request.json
        offer = Offer.query.get(of_id)
        offer.order_id = new_data['order_id']
        offer.executor_id = new_data['executor_id']
        db.session.add(offer)
        db.session.commit()
        return '', 200

    elif request.method == 'DELETE':
        offer = Offer.query.get(of_id)
        db.session.delete(offer)
        db.session.commit()
        return '', 200


if __name__ == '__main__':
    with app.app_context():
        main()
