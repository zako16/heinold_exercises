"""
Ask the user to enter a temperature in Celsius. The program should print a message based
on the temperature:
• If the temperature is less than -273.15, print that the temperature is invalid because it is
below absolute zero.
• If it is exactly -273.15, print that the temperature is absolute 0.
• If the temperature is between -273.15 and 0, print that the temperature is below freezing.
• If it is 0, print that the temperature is at the freezing point.
• If it is between 0 and 100, print that the temperature is in the normal range.
• If it is 100, print that the temperature is at the boiling point.
• If it is above 100, print that the temperature is above the boiling point.
"""
temperature = eval(input("Enter a temperature: "))
if temperature < -273.15:
    message = "Temperature is invalid because it is below absolute zero."
elif temperature == -273.15:
    message = "Temperature is absolute 0."
elif temperature > -273.15 and temperature < 0:
    message = "Temperature is below freezing."
elif temperature == 0:
    message = "Temperature is at the freezing point."
elif temperature > 0 and temperature < 100:
    message = "Temperature is in the normal range."
elif temperature == 100:
    message = "Temperature is at the boiling point."
elif temperature > 100:
    message = "Temperature is above the boiling point."
else:
    message = "Error entry"

print(message)
