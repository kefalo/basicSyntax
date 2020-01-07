# name = input("Please enter your name: ")
# age = int(input("How old are you, {}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enouth to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else: #guess must be greater than 5
        print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("You guessed it wrong")
else:
    print("You got it first time")

age = int(input("How old are you? "))

#if (age >=16) and (age <=65): - code on the line above does the same
if 16 < age < 66:
    print("Have a good day at work")
if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")
