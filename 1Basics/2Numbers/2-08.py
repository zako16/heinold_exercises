"""
Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the operator to get seconds.]
"""
seconds = eval(input("Enter number of seconds:"))
minutes = seconds // 60
seconds = seconds % 60
print("There is ", minutes, "min and ", seconds, "sec")
