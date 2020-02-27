"""
Some built-in functions

max(): It takes any number of arguments and returns the largest one.

min(): It takes any number of arguments and returns the smallest one.

abs(): It returns the absolute value of the number, that number's distance from 0.
It always returns a positive value and it only takes a single number.

type(): It returns the type of the data it receives as an argument.
"""

def largest_number(*args):
    return (max(args))

print(largest_number(-10,0,10,555))

def smallest_number(*args):
    return (min(args))

print(smallest_number(-9,0,5,999))


def abs_function(a):
    print(abs(a))

abs_function(-10)


def type_function(a):
    print(type(a))

type_function(11)
type_function(False)
type_function("Stefan")

l = [1, 2, 3]

type_function(l)