from math import sqrt


class Calculator():
    def __init__(self) -> None:
        pass

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
        return sqrt(a)
    
    def logarithm(self, num, base):
        return 1 + self.logarithm(num / base, base) if (num > base - 1) else 0

# Bhaskara I's sine approximation formula.
    def sine(self, x):
        if (x < 0 or x > 180):
            raise ValueError('Sine must have angle between 0 and 180 deg.')
        else:
            inter = 180 - x
            return (4 * x * inter) / (40500 - x * inter)