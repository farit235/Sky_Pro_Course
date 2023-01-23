import random

questions = [{
"q": "How many days do we have in a week?",
"d": "1",
"a": "7"
}, {
"q": "How many letters are there in the English alphabet?",
"d": "3",
"a": "26"
}, {
"q": "How many sides are there in a triangle?",
"d": "2",
"a": "3"
}, {
"q": "How many years are there in one Millennium?",
"d": "2",
"a": "1000"
}, {
"q": "How many sides does hexagon have?",
"d": "4",
"a": "6"
}]


class Question:

    def __init__(self, text, complexity, right_answer, score, asked=False, answer=None):
        self.text = text
        self.complexity = complexity
        self.right_answer = right_answer
        self.asked = asked
        self.answer = answer
        self.score = score

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов."""
        self.score = int(self.complexity)*10
        return self.score

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает с верным ответов иначе False."""
        return self.right_answer == self.answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Bonpoc: What do people often call American flag?
        Сложность: 4/5"""
        print(f"Вопрос: {self.text}\n"
              f"Сложность: {self.complexity}/5\n")

    def build_positive_feedback(self):
        """Возвращает : Ответ верный, получено __ баллов"""
        print(f"Ответ верный, получено {self.get_points()} баллов\n")

    def build_negative_feedback(self):
        """Возвращает : Ответ неверный, правильный ответ __ """
        print(f"Ответ неверный, верный ответ - {self.right_answer}\n")


def statistics(questions):
    """Статистика по ответам"""
    score = 0
    right_answers = 0
    for i in range(len(questions)):
        score += questions[i].score
        if questions[i].is_correct():
            right_answers += 1

    print(f"Вот и все!\n"
          f"Отвеченo на {right_answers} вопроса из {len(questions)}\n"
          f"Набрано {score} баллов")


def create_list(questions):
    """Создание списка экземпляров объекта"""
    questions_instance = [Question(f"{questions[i]['q']}", f"{questions[i]['d']}", f"{questions[i]['a']}", score=0) for
                          i in range(len(questions))]
    return questions_instance


def game(questions):
    """Функция самой игры"""
    done_questions = []
    for i in range(len(questions)):
        questions[i].build_question()
        questions[i].answer = input("Введите ответ: ")
        is_correct = questions[i].is_correct()
        if is_correct:
            questions[i].build_positive_feedback()
        else:
            questions[i].build_negative_feedback()
        done_questions.append(questions[i])
    return done_questions


random.shuffle(questions)
questions = create_list(questions)
questions = game(questions)
statistics(questions)
