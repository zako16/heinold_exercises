"""
Write a program that asks the user to enter an angle between −180 ◦ and 180 ◦ . Using an
expression with the modulo operator, convert the angle to its equivalent between 0 ◦ and
360 ◦ .
"""
gradus = eval(input("Enter an angle between −180◦ and 180◦ :"))
gradus = abs(gradus) + 180
print("An angle: ", gradus)
