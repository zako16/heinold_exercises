"""
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not.
"""
year = eval(input("Enter year:"))
if ((year % 4 == 0) and(year % 100 != 0)) or (year % 400 == 0):
    print("Year is leap")
else:
    print("Year is not leap")
