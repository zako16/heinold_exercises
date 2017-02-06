"""
Write a program that asks the user to enter a string s and then converts s to lowercase,
removes all the periods and commas from s , and prints the resulting string.
"""
s = input('Enter your string:')
s = s.lower()
comma = '.'
result = ''
period = ''
periodbef = ''
for i in range(len(s)):
    if i < len(s) - 1:
        j = i + 1
        period = s[j]
    if s[i] == period or i == j:
        continue
    if s[i] == comma:
        continue
    result += s[i]
print(result)
