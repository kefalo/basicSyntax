"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
iterable items are Strings, List, Tuple, Dictionary
"""

# x = 0
# while x < 10:
#     print("Loop has value of: " + str(x))
#     x = x + 1
#     print("one more line")

l = []
num = 0
while num < 10:
    l.append(num)
    num +=1
    print("Value of num is: " + str(num))

print(l)