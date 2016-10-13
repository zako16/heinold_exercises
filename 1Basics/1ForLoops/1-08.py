"""
Write a program that asks the user for their name and how many times to print it. The pro-
gram should print out the user’s name the specified number of times.
"""
name = input("Enter your name: ")
n = eval(input("Enter count: "))

for i in range(n):
    print(name)
