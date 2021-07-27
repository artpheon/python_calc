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
            self.sine,
            self.cosine,
            self.tang]

    def resultDecorator(func):
        def wrap(self, a, b):
            print('Result of the operation:', func(self, a, b), '\n')

        return wrap

    def resultDecorator_2(func):
        def wrap(self, a):
            print('Result of the operation:', func(self, a), '\n')

        return wrap

    @resultDecorator
    def sum(self, a, b):
        return a + b

    @resultDecorator
    def sub(self, a, b):
        return a - b

    @resultDecorator
    def mult(self, a, b):
        return a * b

    @resultDecorator
    def div(self, a, b):
        if b == 0:
            raise ValueError('Err: division by zero')
        else:
            return a / b

    @resultDecorator
    def mod(self, a, b):
        if b == 0:
            raise ValueError('Err: division by zero')
        else:
            return a % b

    @resultDecorator
    def power(self, a, b):
        return a ** b

    @resultDecorator_2
    def squareRoot(self, a):
        if a < 0:
            raise ValueError('Err: cannot find sqrt for negative number')
        else:
            return sqrt(a)

    @resultDecorator
    def logarithm(self, num, base):
        if num < 0:
            raise ValueError('Err: cannot find log for negative number')
        if base <= 0:
            raise ValueError('Err: base is negative or zero')
        else:
            # return 1.0 + self.logarithm(num // base, base) if (num > base - 1) else 0
            return log(num, base=base)

    # Bhaskara I's sine approximation formula.
    @resultDecorator_2
    def sine(self, x):
        # if (x < 0 or x > 180):
        #    raise ValueError('Err: sine must have angle between 0 and 180 deg.')
        # else:
        # inter = 180 - x
        # return (4 * x * inter) / (40500 - x * inter)
        return sin(radians(x))

    @resultDecorator_2
    def cosine(self, x):
        # if (x < 0 or x > 180):
        #    raise ValueError('Err: cosine must have angle between 0 and 180 deg.')
        # else:
        # inter = 180 - x
        # return (4 * x * inter) / (40500 - x * inter)
        return cos(radians(x))

    @resultDecorator_2
    def tang(self, x):
        # if (x < 0 or x > 180):
        #    raise ValueError('Err: tangent must have angle between 0 and 180 deg.')
        # else:
        # inter = 180 - x
        # return (4 * x * inter) / (40500 - x * inter)
        return tan(radians(x))
