"""
Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm ,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. An example is shown
below.
Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead? 5
New hour: 1 pm
"""
hour = eval(input("Enter hour:"))
pmam = eval(input("am (1) or pm (2)?"))
ahead = eval(input("How many hours ahead?"))
newHour = (hour + ahead) % 12
newPmam = (hour + ahead) // 12
newPmam = newPmam + pmam
if(newPmam % 2) == 2 or newPmam == 2:
    print("New hour:", newHour, "pm")
elif(newPmam % 2) == 1 or newPmam == 1:
    print("New hour:", newHour, "am")
