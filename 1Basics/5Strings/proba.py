string = input('Enter:')
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