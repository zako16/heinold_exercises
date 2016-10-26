"""
Write a program to compute the sum 1 − 2 + 3 − 4 + · · · + 1999 − 2000 .
"""
summ = 0
for i in range(1, 2001):
    if i % 2 == 0:
        summ -= i
    else:
        summ += i
print("The sum 1−2+3−4+ ··· +1999−2000: ", summ)
