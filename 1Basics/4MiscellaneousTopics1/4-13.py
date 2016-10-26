"""
In the last chapter there was an exercise that asked you to create a multiplication game for
kids. Improve your program from that exercise to keep track of the number of right and
wrong answers. At the end of the program, print a message that varies depending on how
many questions the player got right.
"""
from random import randint
right = 0
notRight = 0
for i in range(10):
    numberOne = randint(1, 10)
    numberTwo = randint(1, 10)
    answer = numberTwo * numberOne
    print("Question: ", numberOne, " x ", numberTwo, " = ", end = "")
    playerNumber = eval(input())
    if answer == playerNumber:
        right += 1
        print("Right")
    elif playerNumber != answer:
        print("Wrong. The answer is ", answer)
notRight = 10 - right
print("You have got", right, "right answers and", notRight, "wrong answers")
