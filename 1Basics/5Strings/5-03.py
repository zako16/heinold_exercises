"""
People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the same number of open-
ing and closing parentheses.
"""
formula = input('Enter a formula: ')
l = '('
r = ')'
countl = 0
countr = 0
for i in formula:
    if i == l:
        countl += 1
    if i == r:
        countr += 1

if countl > countr:
    print('You forget', countl - countr, 'close parantheses')
elif countr > countl:
    print('You forget', countr - countl, 'open parantheses')
elif countl == countr:
    print('All is right')
