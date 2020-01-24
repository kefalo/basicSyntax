"""
A group of code statements which can perform some specific task
Methods group of code statements, which will going to complete some kind of workflow and into one logical entity
"""

def sumNums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

string_add = sumNums('one', 'two')
print(string_add)

sum1 = sumNums(2, 8)

sum2 = sumNums(6, 6)

print(sum1)
print("*"*30)
def isMetro(city):
    l = ['NS', 'BG', 'KG']

    if city in l:
        return True
    else:
        return False

x = isMetro('NS')
print(x)