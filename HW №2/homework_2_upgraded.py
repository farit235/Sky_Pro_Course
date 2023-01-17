print("Hello! Let's check your English skills!")
ready = input("Are you ready to check your skills?")

points = 0
right = 0
score = 0

questions = ["My name _ Vova!", "I _ a coder!", "I live _ Moscow!"]
index_q = range(len(questions))

answers = ["is", "am", "in"]

if ready == "ready":
    for index in index_q:
        attempts = 3
        while attempts != 0:
            print(questions[index])
            answer = input("Answer is: ")
            if answer == answers[index]:
                print("Right!")
                right += 1
                score += attempts
                break
            else:
                print(f"Wrong! You have {attempts-1} attempts!")
            attempts = attempts - 1
            if attempts == 0:
                print(f"Correct answer is: {answers[index]}")
    print(f"That's all! You've answered on {right} questions from {len(index_q)} true, that's {round(right/len(index_q) * 100, 2)}%! Your score is {score} out of {12}")
else:
    print("It looks, that you don't want to play the game!")