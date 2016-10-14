"""
Write a program that asks the user to enter an angle in degrees and prints out the sine of that
angle.
"""
from math import sin, radians
angle = eval(input("Enter an angle in degrees:"))
sinOfAngle = round(sin(radians(angle)), 2)
print("Sin:", sinOfAngle)
