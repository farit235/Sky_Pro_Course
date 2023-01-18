import random


def read_word(filename, record_=0):
    """Функция чтения слов из файла и игра"""
    with open(filename) as file:
        for line in file:
            line = line.strip()
            shuffle_word = ''.join(random.sample(line, len(line)))
            print(shuffle_word)
            input_word = input("Введите ответ: ")
            if input_word == line:
                print("Верно! Вы получаете 10 очков!")
                record_ += 10
            else:
                print(f"Неверно, верный ответ - {line}")
    return record_


def read_top_players(name_):
    """Функция чтения топа игроков"""
    with open("history.txt") as file:
        top_score_ = 0
        game_counter = 0
        for line in file:
            player_data = line.strip().split(" ")
            if player_data[0] == name_:
                game_counter += 1
                if int(player_data[1]) > top_score_:
                    top_score_ = int(player_data[1])
    return top_score_, game_counter


def write_players(name_, record_):
    """Функция записи в топ игроков"""
    with open("history.txt", "a") as file:
        file.write(name_ + " " + str(record_) + "\n")


name = input("Введите Ваше имя: ")
record = read_word("words.txt")
write_players(name, record)
top_score, counter = read_top_players(name)

print(f"Всего сыграно игр: {counter}\n"
      f"Максимпльный рекорд: {top_score}")
