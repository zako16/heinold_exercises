"""
Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
cubes, or perfect fifth powers.
"""
from math import sqrt, trunc
count = 0
for i in range(1, 1001):
    squareOfDivisor = sqrt(i)
    truncOfDivisor = trunc(squareOfDivisor)
    if squareOfDivisor == truncOfDivisor:
        squareNum = i
        count += 1
    number = i
    if squareNum == number:
        continue
    else:
        for j in range(1, number + 1):
            if (number % j == 0) and (pow(j, 3) == number):
                count += 1
                cubeNum = i
    if squareNum == i and cubeNum == i:
        continue
    else:
        for j in range(1, number + 1):
            if number % j == 0 and pow(j, 5) == number:
                count += 1
print(count)
