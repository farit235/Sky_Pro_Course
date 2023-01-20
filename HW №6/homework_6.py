import json


def check_info(questions_):
    """Функция для проверки правильно введенной информации"""
    type_list = []
    points_list = []
    for type_, data in questions_.items():
        type_list.append(type_)
        for key in data:
            points_list.append(int(key))
    return type_list, list(set(points_list))


def load_questions(filename_):
    """Функция, которая загружает вопросы из файла '.json'"""
    with open(filename_) as file:
        questions_ = json.load(file)
    return questions_


def show_fields(questions_):
    """Функция, которая выводит игровое поле"""
    len_type = 0
    for type_, data in questions_.items():
        points = []
        if len(type_) > len_type:
            len_type = len(type_)
        for key, value in data.items():
            if value['asked']:
                key = "   "
            points.append(key)

        print(type_ + (len_type-len(type_))*" ", points[0], points[1], points[2])


def parse_input(type_list_, points_list_):
    """Функция, которая делит ввод пользователя на текст и число"""
    while True:
        input_text = input("Введите текст для игры: ")
        category, number = input_text.split(" ")
        if (category == type_list_[0] or category == type_list_[1] or category == type_list_[2]) and (int(number) == points_list_[0] or int(number) == points_list_[1] or int(number) == points_list_[2]):
            print()
            break
        else:
            print("Wrong type! Try one more time!")
    return category, int(number)


def show_question(questions_, category_, number_, score_, right_answers_, wrong_answers_):
    """Функция, которая печатает вопрос"""
    word = input(f"Слово {questions_[category_][str(number_)]['question']} означает - ")
    if word == questions_[category_][str(number_)]['answer']:
        questions_[category_][str(number_)]['asked'] = True
        score_ += number_
        right_answers_ += 1
        print(f"Верно! Вы получили {str(number_)} очков! У Вас {score_} очков.\n")
    else:
        score_ -= number_
        wrong_answers_ += 1
        print(f"Неверно! Попробуйте позже еще раз! У Вас {number_} очков. У Вас {score_} очков.\n")
    return score_, right_answers_, wrong_answers_


def show_stats(score_, right_answers_, wrong_answers_):
    """Функция, которая печатает статистику"""
    print(f"Ваш счет: {score_}\n"
          f"Количество правильных ответов: {right_answers_}\n"
          f"Количество неправильных ответов: {wrong_answers_}\n")


def save_results_to_file(score_, right_answers_, wrong_answers_):
    """Функция, которая сохраняет статистику в json-файл"""
    result = {"points": str(score_), "correct": str(right_answers_), "incorect": str(wrong_answers_)}
    with open("results.json", "w") as file:
        file.write(json.dumps(result))


score = 0
right_answers = 0
wrong_answers = 0
all_asked = 9
questions = load_questions("questions.json")
type_list, points_list = check_info(questions)

while True:
    show_fields(questions)
    category, number = parse_input(type_list, points_list)
    score, right_answers, wrong_answers = show_question(questions, category, number, score, right_answers, wrong_answers)
    show_stats(score, right_answers, wrong_answers)
    asked = 0
    for k, v in questions.items():
        for key, value in v.items():
            if value['asked']:
                asked += 1
        if asked == all_asked:
            save_results_to_file(score, right_answers, wrong_answers)
            print("Игра успешно пройдена")
            exit(0)
