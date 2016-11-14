"""
Write a program that asks the user to enter a string. The program should then print the
following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e
(k) The string with every letter replaced by a space
"""
string = input("Enter string: ")
# a: total number of characters
a_count = 0
for i in string:
    if i.isalpha():
        a_count += 1
print("The total number of characters:", a_count)
# b: string repeated 10 times
print('b', "-"*10)
for i in range(10):
    print(string)
# c first character of the string (remember that string indices start at 0)
print('c', "-"*10)
for i in string:
    if i.isalpha():
        print(i)
        break
# d first three characters of the string
print('d', "-"*10)
c_count = 0
c_string = ''
for i in string:
    if i.isalpha():
        c_string += i
        c_count += 1
    if c_count == 3:
        break
print(c_string)
# e last three characters of the string
print('e', "-"*10)
c_count = 0
c_string = ''
for i in string[::-1]:
    if i.isalpha():
        c_string += i
        c_count += 1
    if c_count == 3:
        break
print(c_string)
# f string backwards
print('f', "-"*10)
f_string = string[::-1]
print(f_string)
# g seventh character of the string if the string is long enough and a message otherwise
print('g', "-"*10)
g_len = len(string)
if g_len >= 16:
    if string[16].isalpha():
        print("Is string")
    else:
        print('Not aplha')
else:
    print('String not enough long')
# h string with its first and last characters removed
print('h', "-"*10)
h_string = ''
h_first = 0
h_last = 0
for i in range(len(string)):
    if string[i].isalpha():
        h_first = i
        break
for i in range(len(string)-1, 0-1, -1):
    if string[i].isalpha():
        h_last = i
        break
h_string = string[:h_first]
h_string += string[h_first+1:h_last]
h_string += string[h_last+1:]
print(h_string)
# i string in all caps
print('i', "-"*10)
i_string = string
i_string = i_string.upper()
print(i_string)
# j string with every a replaced with an e
print('j', "-"*10)
j_string = string
if 'a' in j_string:
    j_string.replace('a', 'e')
print(j_string)
# k string with every letter replaced by a space
print('k', "-"*10)
k_string = string
for i in range(len(k_string)):
    if k_string[i].isalpha():
        k_string[i].replace(k_string[i], 'a')
print(k_string)
