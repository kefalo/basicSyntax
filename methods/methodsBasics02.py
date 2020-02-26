"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value
"""

def sum_nums(n1=1, n2=4):
    """
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum1 = sum_nums(8, n2=50)
print(sum1)