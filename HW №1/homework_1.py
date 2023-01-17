print("Hello! Let's check your English skills!")
name = input("Type your name: ")

points = 0


answer_1 = input("My name _ Vova!")
if answer_1 == "is":
    points += 10
    print("Right answer! You've earned 10 points!")
else:
    print("Wrong! Right answer: 'is'")

answer_2 = input("I _ a coder!")
if answer_2 == "am":
    points += 10
    print("Right answer! You've earned 10 points!")
else:
    print("Wrong! Right answer: 'am'")

answer_3 = input("I live _ Moscow!")
if answer_3 == "in":
    points += 10
    print("Right answer! You've earned 10 points!")
else:
    print("Wrong! Right answer: 'in'")


print(f"End of the test, {name}\n"
      f"You've answered on {points//10} of 3\n"
      f"You've earned {points} points\n"
      f"That's {round((points/3)*10, 2)}%")