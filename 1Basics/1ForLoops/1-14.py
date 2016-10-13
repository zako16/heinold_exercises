"""
Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.
   *
  ***
 *****
*******
 *****
  ***
   *
"""
high = eval(input("How high the box should be:"))
high = int(high / 2)

for i in range(high):
    print(" "*(high-i), "*"*i + "*"*(i-1))

for i in range(high):
    print(" "*i, "*"*(high-i) + "*"*(high-i-1))
