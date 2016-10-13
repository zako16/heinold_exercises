"""
Use a for loop to print an upside down triangle like the one below. Allow the user to specify
how high the triangle should be.
****
***
**
*
"""
high = eval(input("How high the box should be:"))
for i in range(high, 0, -1):
    print("*"*i)
