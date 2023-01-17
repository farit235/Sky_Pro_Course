import random


def morse_encode(sentence):
    """Переводит слова на английском в азбуку морзе"""
    encoded_sentence = ""
    for letter in sentence:
        encoded_sentence = encoded_sentence + codes.get(letter)
    return encoded_sentence


def get_word(phrases_):
    """Получает случайное слово из списка"""
    random.shuffle(phrases_)
    phrase = phrases_[0]
    return phrase


def print_statistics(answers_):
    """Выводит статистику списка"""
    all_ans = 0
    right_ans = 0
    wrong_ans = 0
    for answer in answers_:
        all_ans += 1
        if answer:
            right_ans += 1
        else:
            wrong_ans += 1

    print(f"Всего задачек: {all_ans}\n"
          f"Отвечено верно: {right_ans}\n"
          f"Отвечено неверно: {wrong_ans}\n")


answers = []
phrases = ["code", "bit", "list", "soul", "next"]
codes = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
         "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
         "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
         "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
         "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.",
         "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}
counter = 0

input("Сегодня мы потренеруемся расшифровывать азбуку морзе!\n"
      "Нажмите Enter и мы начнем")

for i in range(0, 5):
    counter += 1
    word = get_word(phrases)
    encoded_text = morse_encode(word)
    print(f"Слово {counter} - {encoded_text}")
    word_inp = input("Введите слово: ")
    encoded_text_p = morse_encode(word_inp)
    if encoded_text == encoded_text_p:
        answers.append(True)
    else:
        answers.append(False)

print_statistics(answers)
