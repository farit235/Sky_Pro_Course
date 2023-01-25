import json
from json import JSONDecodeError
import logging

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

logging.basicConfig(filename="basic.log", level=logging.INFO)
logging.basicConfig(filename="basic.log", level=logging.ERROR)


def read_data():
    """Функция чтения из файла"""
    try:
        with open('posts.json', 'r') as file:
            data = json.loads(file.read())
        return data
    except FileNotFoundError:
        logging.error("Файла json в проекте нет!")
        print("Файла json в проекте нет!")
    except JSONDecodeError:
        print("Файл неудается преобразовать")


def find_items(word, data=read_data()):
    """Функция поиска в данных из файла"""
    try:
        logging.info("Поиск по всем строчкам файла")
        posts_list = []
        for item in data:
            if word in item['content']:
                posts_list.append(item)
        return posts_list
    except TypeError:
        logging.error("Ошибка чтения файла!")


def add_to_json(text, picture):
    """Функция добавления данных в json файл"""
    extension = picture.filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        data_item = {"pic": f"{picture.filename}",
                     "content": f"{text}"}
        data = read_data()
        data.append(data_item)
        with open('posts.json', 'w') as file:
            file.write(json.dumps(data, ensure_ascii=False))
    else:
        logging.info("Используете неправльный тип файла")
        print("Используете неправльный тип файла")
