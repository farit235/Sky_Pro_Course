print("Hello! Let's check your English skills!")
ready = input("Are you ready to check your skills?")

points = 0
questions = ["My name _ Vova!", "I _ a coder!", "I live _ Moscow!"]
answers = ["is", "am", "in"]
index_q = range(len(questions))
right = 0


if ready == "ready":
    for index in index_q:
        print(questions[index])
        answer = input("Answer is: ")
        if answer == answers[index]:
            print("Right!")
            right += 1
        else:
            print("Wrong!")
    print(f"That's all! You've answered on {right} questions from {len(index_q)} true, that's {round(right/len(index_q) * 100, 2)}%")
else:
    print("It looks, that you don't want to play the game!")