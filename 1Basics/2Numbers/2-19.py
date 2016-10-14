"""
Write a program that draws “modular rectangles” like the ones below. The user specifies the
width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5
rectangle and a 4 × 8 .
"""
wide = eval(input("Enter wide:"))
high = eval(input("Enter high:"))
count = 0
for i in range(high):
    for j in range(wide):
        print(count % 10, end=" ")
        count += 1
    print(end="\n")
