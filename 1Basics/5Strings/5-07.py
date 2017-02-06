"""
Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards.
"""
word = input('Enter a word:')
palindrome = word[::-1]
if word == palindrome:
    print('Palindrome')
else:
    print('Not palindrome')
