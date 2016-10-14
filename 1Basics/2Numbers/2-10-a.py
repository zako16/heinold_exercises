"""
(a) One way to find out the last digit of a number is to mod the number by 10. Write a
program that asks the user to enter a power. Then find the last digit of 2 raised to that
power.
"""
from math import pow
power = eval(input("Enter a power:"))
resheniye = pow(2, power)
resheniye = resheniye % 10
print(resheniye)
