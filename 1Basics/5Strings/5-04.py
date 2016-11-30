"""
Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.
"""
word = input("Enter a word:")
vowels = False

if 'a' in word or 'i' in word or 'o' in word or 'e' in word or 'u' in word:
    vowels = True

if vowels is True:
    print('Vowels exist')
if vowels is False:
    print('There are no one vowels')
