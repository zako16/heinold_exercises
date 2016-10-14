"""
(b) One way to find out the last two digits of a number is to mod the number by 100. Write
a program that asks the user to enter a power. Then find the last two digits of 2 raised to
that power.
"""
from math import pow
power = eval(input("Enter a power:"))
resheniye = pow(2, power)
resheniye = resheniye % 100
print(resheniye)
