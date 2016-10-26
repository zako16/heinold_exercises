"""
Write a program that counts how many of the squares of the
numbers from 1 to 100 end in a 1.
"""
count = 0
for i in range(1, 100):
    square = i * i
    if square % 10 == 1:
        print(square, " = ", i, " * ", i)
        count += 1

print("The squares of the numbers from 1 to 100 end in a 1: ", count)
