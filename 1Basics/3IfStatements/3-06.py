"""
A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost.
"""
item = eval(input("Enter how many items are you buying:"))
if item < 10:
    cost = 12
elif item >= 10 and item <= 99:
    cost = 10
elif item >= 100:
    cost = 7

total = 0
for i in range(1, item):
    total += cost

print("Total cost of", item, "items: ", total, "$")
