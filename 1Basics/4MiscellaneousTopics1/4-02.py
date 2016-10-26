"""
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9.
"""
count4 = 0
count9 = 0
for i in range(1, 100):
    square = i * i
    if square % 10 == 4:
        count4 += 1
    if square % 10 == 9:
        count9 += 1

print("The squares of the numbers from 1 to 100 end in a 4: ", count4)
print("The squares of the numbers from 1 to 100 end in a 9: ", count9)
