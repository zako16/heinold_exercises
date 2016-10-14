"""
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temper-
ature is in. Your program should convert the temperature to the other unit. The conversions
are F = 9/5 * C + 32 and C = 9/5*(F − 32) .
"""
temperature = eval(input("Enter a temperature:"))
unit = input("Enter C - Celsius; Enter F - Fahrenheit:")
if unit[0] == "C":
    temperature = ((9/5)*temperature)+32
    print("Temperature from Celsius to Fahrenheit: ", temperature)
elif unit[0] == "F":
    temperature = (9/5)*(temperature-32)
    print("Temperature from Fahrenheit to Celsius: ", temperature)
else:
    print("Entry is invalid")
