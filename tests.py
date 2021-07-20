import math
from calc import Calculator

def testCalculator(a, b):
    c = Calculator()
    print('_____________________\nTest for nums', a, b)
    print('Sum: ', c.sum(a, b), "and", a + b)
    print('Sub: ', c.sub(a, b), 'and', a - b)
    print('Mult: ', c.mult(a, b), 'and', a * b)
    try:
        print('Div: ', c.div(a, b), 'and', a / b)
    except ValueError as e:
        print('Div:', e.args[0])
    try:
        print('Mod: ', c.mod(a, b), 'and', math.modf(a))
    except ValueError as e:
        print('Mod:', e.args[0])
    print('Pow: ', c.power(a, b), 'and', math.pow(a, b))
    try:
        print('Sqrt: ', c.squareRoot(a), 'and', math.sqrt(a))
    except ValueError as e:
        print('Sqrt:', e.args[0])
    try:
        print('Log: ', c.logarithm(a, b), 'and', math.log(a, b))
    except ValueError as e:
        print('Log:', e.args[0])
    try:
        print('Sin: ', c.sine(a), 'and', math.sin(a))
    except ValueError as e:
        print('Sin:', e.args[0])
    

def runTests():
    testCalculator(-1, 3)
    testCalculator(0, 0)
    testCalculator(5, -2)
    testCalculator(6, 0)
    testCalculator(6, 6)
    testCalculator(6, 6)
    testCalculator(30, 6)