"""
Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be.
*******************
*******************
*******************
*******************
"""
wide = eval(input("How wide the box should be: "))
high = eval(input("How high the box should be:"))
for i in range(high):
    print("*"*wide)
