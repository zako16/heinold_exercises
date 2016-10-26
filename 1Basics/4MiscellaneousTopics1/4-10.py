"""
Ask the user to enter 10 test scores. Write a program to do the following:
(a) Print out the highest and lowest scores.
(b) Print out the average of the scores.
(c) Print out the second largest score.
(d) If any of the scores is greater than 100, then after all the scores have been entered, print
a message warning the user that a value over 100 has been entered.
(e) Drop the two lowest scores and print out the average of the rest of them.
"""
from random import randint
scores = []
for i in range(10):
    f = i + 1
    score = eval(input("Enter %s score:" % f))
    # score = randint(1, 9)
    # print(score)
    scores.append(score)
highest = scores[0]
lowest = scores[0]
secondHighest = scores[0]
secondLowest = scores[0]
lowestIndex = 0
secondLowestIndex = 0
summ = 0
moreThenHundred = 0
for i in range(10):
    summ += scores[i]
    if highest < scores[i]:
        highest = scores[i]
    if lowest > scores[i]:
        lowest = scores[i]
        lowestIndex = i
    if scores[i] >= 100:
        moreThenHundred = 1
for i in range(10):
    if secondHighest < scores[i] and scores[i] < highest:
        secondHighest = scores[i]
    if secondLowest < scores[i] and scores[i] <= lowest:
        secondLowest = scores[i]
        secondLowestIndex = i
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average of scores:", summ / 10)
print("Second highest score:", secondHighest)
if moreThenHundred == 1:
    print("Was entered score more then 100")
scores[lowestIndex] = 0
scores[secondLowestIndex] = 0
summ = 0
for i in range(10):
    summ += scores[i]
print("Average of scores, drop two lowest:", summ / 10)
