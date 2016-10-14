"""
Write a program that asks the user how many credits they have taken. If they have taken less
than 23, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and seniors are 84 and over.
"""
credits = eval(input("How many credits you have taken:"))
if credits > 0 and credits <= 23:
    message = "You are freshman"
elif credits >= 24 and credits <= 53:
    message = "You are sophomore"
elif credits >= 54 and credits <= 83:
    message = "You are juniors"
elif credits >= 84:
    message = "You are seniors"
else:
    message = "Entry is invalid"
print(message)
