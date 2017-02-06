"""
Write a program that asks the user to enter a string. The program should create a new string
called new_string from the user’s string such that the second character is changed to an
asterisk and three exclamation points are attached to the end of the string. Finally, print
new_string . Typical output is shown below:
Enter your string: Qbert
Q*ert!!!
"""
user_string = input('Enter your string:')
new_string = user_string[:1]
new_string += '*'
new_string += user_string[2:]
new_string += '!!!'
print(new_string)
