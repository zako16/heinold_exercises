"""
Write a program that generates a random decimal number between 1 and 10 with two decimal
places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.
"""
from random import randint
randec = randint(1, 10)
randec2 = randint(1, 100)
randec2 = randec2/100
randecimal = randec + randec2
print(randecimal)
