"""
Write a program that asks the user to enter two numbers, x and y , and computes
|x− y| / (x+y).
"""
x_number = eval(input("Enter x:"))
y_number = eval(input("Enter y:"))
reshenie = abs(x_number - y_number) / (x_number + y_number)
print("|x− y|/(x+y) = ", reshenie)
