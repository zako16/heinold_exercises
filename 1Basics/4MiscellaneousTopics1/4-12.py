"""
Write a program that asks the user to guess a random number between 1 and 10. If they guess
right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
the user five numbers to guess and print their score after all the guessing is done.
"""
from random import randint
score = 0
for i in range(5):
    randNumber = randint(1, 10)
    userNumber = eval(input("Enter a number between 1 and 10:"))
    if randNumber == userNumber:
        score += 10
        print("WIN")
    elif randint != userNumber:
        score -= 1
        print("You loose")
print("Your score:", score)
