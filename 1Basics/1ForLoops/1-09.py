"""
The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .
"""
n = eval(input("How many Fibonacci numbers to print: "))
fp = 1
f = 1
print(fp, end=", ")
print(f, end=", ")
for i in range(n-2):
    ff = f + fp
    f = fp
    fp = ff
    print(ff, end=", ")
print("")
