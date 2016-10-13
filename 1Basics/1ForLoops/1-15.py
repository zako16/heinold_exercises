"""
Write a program that prints a giant letter A like the one below. Allow the user to specify how
large the letter should be.
    *
   * *
  *****
 *     *
*       *
"""
high = eval(input("How high the box should be:"))
h = int(high/2)
for i in range(h):
    p = high-i
    print(" "*(p), "*" + " "*(i*2) + "*")

print(" "*(p-1), "*"*4+"*"*(i*2))

for i in range(h+1, high):
    p = high-i
    print(" "*(p), "*" + " "*(i*2) + "*")
