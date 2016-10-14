"""
(c) Write a program that asks the user to enter a power and how many digits they want.
Find the last that many digits of 2 raised to the power the user entered.
"""
from math import pow
power = eval(input("Enter a power:"))
modulo = eval(input("Enter a digits:"))
resheniye = pow(2, power)
resheniye = resheniye % modulo
print(resheniye)
