"""
Write a program that generates a random number, x , between 1 and 50, a random number y
between 2 and 5, and computes x y .
"""
from random import randint
x_number = randint(1, 50)
y_number = randint(2, 5)
exp = x_number ** y_number
print(x_number, " ^ ", y_number, " = ", exp)
