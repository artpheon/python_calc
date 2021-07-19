from .Calculator import Calculator

def testCalculator(a, b):
    c = Calculator
    print('Sum: ' + c.sum(a, b))
    print('Sub: ' + c.sum(a, b))
    print('Mult: ' + c.sum(a, b))
    try:
        print('Div: ' + c.sum(a, b))
    except ValueError:
        print('No division by zero!')
    try:
        print('Mod: ' + c.sum(a, b))
    except ValueError:
        print('No division by zero!')
    print('Pow: ' + c.sum(a, b))
    print('Sqrt: ' + c.sum(a, b))
    print('Log: ' + c.sum(a, b))
    

def start(a, b):
    
