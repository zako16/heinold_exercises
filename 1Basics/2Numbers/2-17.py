"""
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year.
"""
thatYear = eval(input("Enter that year:"))
count = (thatYear - 1600)//4

cen = (thatYear - 1600)//100
cen400 = 0
for i in range(1600, thatYear, 100):
    cen400 += 1
print("Leap years count:", count - cen + cen400)
