"""
Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie.
"""
from random import randint
computer = 0
human = 0
for i in range(5):
    print("Rock=0; Paper=1; Scissors=2;")
    computerPlay = randint(0, 2)
    humanPlay = eval(input("Your enter:"))
    print("Computer:", computerPlay)
    if computerPlay == humanPlay:
        continue
    elif computerPlay == 0 and humanPlay == 2:
        computer += 1
    elif computerPlay == 2 and humanPlay == 0:
        human += 1
    elif computerPlay < humanPlay:
        human += 1
    elif computerPlay > humanPlay:
        computer += 1

if computer > human:
    print("You lost! Computer:", computer, "; You:", human)
elif computer < human:
    print("You win!! You:", human, "; Computer:", computer)
elif computer == human:
    print("Tie")
