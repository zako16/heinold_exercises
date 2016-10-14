"""
Write a program that asks the user for a number and prints out the factorial of that number.
"""
from math import factorial
number = eval(input("Enter a number:"))
factorialOfNumber = factorial(number)
print("Factorial:", factorialOfNumber)
