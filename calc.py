from math import *

class Calculator(object):
    def __init__(self) -> None:
        self.operations = [
            self.sum,
            self.sub,
            self.mult,
            self.div,
            self.mod,
            self.power,
            self.squareRoot,
            self.logarithm,
            self.sine]

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError('Division by zero')
        else:
            return a / b

    def mod(self, a, b):
        if b == 0:
            raise ValueError('Division by zero')
        else:
            return a % b

    def power(self, a, b):
        return a ** b
    
    def squareRoot(self, a):
        if a < 0:
            raise ValueError('Cannot find sqrt for negative number')
        else:
            return sqrt(a)
    
    def logarithm(self, num, base):
        if num < 0:
            raise ValueError('Cannot find log for negative number')
        if base <= 0:
            raise ValueError('Base is negative or zero')
        else:
            return 1.0 + self.logarithm(num // base, base) if (num > base - 1) else 0

# Bhaskara I's sine approximation formula.
    def sine(self, x):
        if (x < 0 or x > 180):
            raise ValueError('Sine must have angle between 0 and 180 deg.')
        else:
            inter = 180 - x
            return (4 * x * inter) / (40500 - x * inter)
    
    #listing
