"""
Methods Excercise
Create a method which takes the state and grass income as the arguments and retuyrns the net income after deducting tax basedon the state.

Assume Federal Tax: 10%
Define State tax on free will

You don't have to do for all the states, just take 3, 4 to solve the purpose of this excercise.
"""

def tax_of_states(gross, state):
    """
    Calculate the net income after federal and state tax
    :param gross: Gross income - person's income
    :param state: State Name
    :return: Net income
    """
    state_tax = {'NS':10, 'BG':15, 'ZR':5}

    #Calculate net income after federal tax
    net = gross - (gross * .10)

    #Calculate net icnome after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net income after the heavy taxes is: " + str(net))
        return net
    else:
        print("State not in the list")
        return None

tax_of_states(12000,'NS')