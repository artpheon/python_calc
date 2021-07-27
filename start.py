import math
from calc import Calculator
from tests import *


def promptCalculator():
    c = Calculator()
    while True:
        try:
            operation = int(input('''
Use the following operations:
0 - Addition
1 - Subtraction
2 - Multiplication
3 - Division
4 - Modulo
5 - Raising in power
6 - Square root
7 - Logarithm
8 - Sine of angle(in degrees)
9 - Cosine of angle(in degrees)
10 - Tangent of angle(in degrees)
Enter the operation: '''))
            print('')
            if 0 > operation or operation > 10:
                raise Exception
        except Exception:
            print('Enter valid operation number..\n')
            continue
        try:
            if operation in (6, 8, 9, 10):
                a = float(input('Enter the value: '))
                c.operations[operation](a)
            else:
                a = float(input('Enter the 1 value: '))
                b = float(input('Enter the 2 value: '))
                c.operations[operation](a, b)
        except Exception as e:
            print(e.args[0], '\n')
        finally:
            ret = input('continue? y/n: ')
            if ret == 'y':
                pass
            else:
                break


def start():
    try:
        promptCalculator()
    except KeyboardInterrupt:
        print('\nExited')


if __name__ == '__main__':
    start()
