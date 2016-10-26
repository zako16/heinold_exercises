"""
Write a program that swaps the values of three variables x , y , and z , so that x gets the value
of y , y gets the value of z , and z gets the value of x .
"""
x, y, z = eval(input("Enter 3 values:"))
hold = x
x = y
y = z
z = hold
print(x, y, z)
