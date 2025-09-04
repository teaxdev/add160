"""
comparison(): compares 2 numbers and gives different outputs based on the arguments
"""

def comparison(number1, number2):
    if number1 > 0 and number2 > 0: # checks if each number is greater than 0
        if number1 > number2: # if  1 is greater than 2, loop the value of 2 and print 1 that many times
            for i in range(number2):
                print(number1)

        else:
            for j in range(number1): # if 2 is greater, it does the opposite
                print(number2)

    elif number1 == 0 or number2 == 0: # if one of the numbers is 0, returns "zero found"
        return "Zero found"
    
    else:
        return number1 - number2  # return and subtract 1 by 2
try:    
    comparison()
except TypeError:
    print("Please input 2 numbers")