"""
Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.
*
**
***
****
"""
high = eval(input("How high the box should be:"))
for i in range(1, high+1):
    print("*"*i)
