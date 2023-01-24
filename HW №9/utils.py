import json


def load_candidates_from_json(path):
    """Функция возвращает список всех кандидатов"""
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    """Функция возвращает кандидата по его id"""
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if int(candidate['id']) == candidate_id:
            return candidate


def get_candidate_by_name(candidate_name):
    """Функция возвращает кандидата по его имени"""
    candidates = load_candidates_from_json("candidates.json")
    candidates_list = []
    for candidate in candidates:
        candidate_fullname = candidate['name'].split()
        if candidate_fullname[0] == candidate_name:
            candidates_list.append(candidate)
    return candidates_list


def get_candidate_by_skill(candidate_skill):
    """Функция возвращает кандидата по его навыкам"""
    candidates = load_candidates_from_json("candidates.json")
    candidates_list = []
    for candidate in candidates:
        skills = candidate['skills'].split(", ")
        if candidate_skill in skills:
            candidates_list.append(candidate)
    return candidates_list
