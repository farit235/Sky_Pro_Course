import json


def load_candidates():
    with open("candidates.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        return data

load_candidates()