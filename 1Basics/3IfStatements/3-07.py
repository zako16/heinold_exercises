"""
Write a program that asks the user for two numbers and prints !Close! if the numbers are
within .001 of each other and !Not close! otherwise.
"""
numberOne = eval(input("Enter 1 number:"))
numberTwo = eval(input("Enter 2 number:"))
if abs(numberOne - numberTwo) <= .001:
    print("Close")
elif abs(numberOne - numberTwo) > .001:
    print("Not close")
