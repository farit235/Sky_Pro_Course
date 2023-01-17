ranks = {0: "Нулевой", 1: "Так себе", 2: "Можно лучше", 3: "Норм", 4: "Хорошо", 5: "Отлично"}
easy = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять"}
medium = {"blue": "голубой", "red": "красный", "white": "белый", "black": "черный", "gray": "серый"}
hard = {"car": "автомобиль", "truck": "грузовик", "pillow": "подушка", "head": "голова", "phone": "телефон"}
answers = {}
words = {}
right_answers = []
wrong_answers = []
rank = 0

level = input("Введите уровень сложности (easy, medium, hard): ")

if level == "easy":
    words = easy
elif level == "medium":
    words = medium
else:
    words = hard

for key, value in words.items():
    print(f"Ключ {key}, длина слова {len(value)}, начинается на {value[0]}...")
    answer = input("Ваш ответ: ")
    if answer == value:
        print(f"Верно! {key.title()} это {value}")
        answers[key] = True
    else:
        print(f"Неверно! {key.title()} это {value}")
        answers[key] = False

for key in answers:
    if answers[key] == True:
        right_answers.append(key)
    else:
        wrong_answers.append(key)

print("Правильные ответы:")
for item in right_answers:
    print(item)
    rank += 1

print()

print("Неправильные ответы")
for item in wrong_answers:
    print(item)

print()

print("Ваш ранг:", ranks[rank])
