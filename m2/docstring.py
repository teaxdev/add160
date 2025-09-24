# Sample Python program without comments and docstrings

""" Simple Python Calculator

    The Calculator class has methods to add, subtract, multiply and divide. Additional methods 
    include clear to reset and get value to return the final calculation.

    Returns:
        _type_: _description_
"""

class Calculator:

    """
        Attributes: 
        value (int): keeps track of what the value that is calculated
    """

    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num

    def subtract(self, num):
        self.value -= num

    def multiply(self, num):
        self.value *= num

    def divide(self, num):
        if num != 0:
            self.value /= num
        else:
            raise ValueError("Cannot divide by zero")
        
    def clear(self):
        self.value = 0

    def get_value(self):
        return self.value
    
def main():

    """
    main(): Calls the math methods from Calculator and prints the final value
    """

    calc = Calculator()
    calc.add(10)
    calc.subtract(2)
    calc.multiply(5)
    # TODO implement input() and a basic UI for easy use
    try:
        calc.divide(0)
    except ValueError as e:
        print(e)

    calc.divide(4)
    # TODO implement the clear method

    print(f"Final value: {calc.get_value()}")
    # help(str)
if __name__ == "__main__":
    main()
