"""
Write a program that asks the user to enter a number and prints the sum of the divisors of
that number. The sum of the divisors of a number is an important function in number theory.
"""
number = eval(input("Enter a value:"))
summ = 0
for i in range(1, number+1):
    if number % i == 0:
        summ += i
print("The summ of divisors:", summ)
