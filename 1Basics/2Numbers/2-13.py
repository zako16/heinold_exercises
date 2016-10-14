"""
Write a program that asks the user for a number and then prints out the sine, cosine, and
tangent of that number.
"""
from math import sin, cos, tan
number = eval(input("Enter a number:"))
sinOfNumber = sin(number)
cosOfNumber = cos(number)
tanOfNumber = tan(number)
print("Sin is ", sinOfNumber, "; Cos is ", cosOfNumber, "; Tan is ", tanOfNumber)
