"""
Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.
"""
centimeters = eval(input("Enter a length in centimeters:"))
if centimeters < 0:
    print("Entry is invalid")
else:
    print(centimeters*2.54, "inches")
