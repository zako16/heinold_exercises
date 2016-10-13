"""
Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 50.
"""
from random import randint
for i in range(1, 50):
    print(randint(1, i))
