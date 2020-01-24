"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""


def sum_nums(n1, n2=6):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(11, n2=11)
print(sum1)
print(sum_nums(11))
