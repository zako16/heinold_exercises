"""
Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
"""
from random import randint
number = randint(1, 10)
guessNumber = eval(input("Enter guess number:"))
if guessNumber == number:
    print("You are right!!!")
elif guessNumber != number:
    print("Not")
