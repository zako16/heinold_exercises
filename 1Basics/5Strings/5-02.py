"""
A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program
"""
sentence = input('Enter a sentence: ')
word = ''

num = 0
for i in sentence:
    if i.isalpha():
        word += i
    else:
        if len(word) >= 2:
            num += 1
        print(word)
        word = ''

print(num)
