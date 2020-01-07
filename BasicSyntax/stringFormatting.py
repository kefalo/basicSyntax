age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31, "January", "March", "May", "July", "August", "October", "December"))


print("""January: {1}
February: {2}
March: {1}
April: {0}
May: {1}
June: {0}
July: {1}
August: {1}
September: {0}
October: {1}
November: {0}
December: {1}""".format(30, 31, 28))
print("/////////////////////////////////")

#python 2 programming examples for formating the strings - we are using %example

print("My age is %d years " % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))
print()

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))

print("Pi is approximately %12.50f" % (22 / 7))

#same result in python 3

for i in range(1, 12):
    print("No. {:2} squared is {:4} and cubed is {:4}".format(i, i**2, i**3))

print("Pi is approximately {0:12.50}".format(22 / 7))