"""
Write a program that asks the user to enter a value n , and then computes (1 +
1/2 + 1/3 +...+1/n) − ln(n) . The ln function is log in the math module.
"""
from math import log
n = eval(input("Enter a value:"))
summ = 0
for i in range(1, n):
    summ += 1/n
solution = summ - log(n)
print("(1+1/2+1/3+...+1/n) − ln(n) = ", solution)
